""""Validators for Drivers App."""

from PIL import Image
from datetime import date, datetime, timedelta
from django.core.validators import BaseValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible


def validate_phone(value):
    """Validate a phone number according to the Chilean format."""
    validator = RegexValidator(
        regex=r"^\+56\d{9}$", message="Invalid phone number.", code="invalid_name"
    )
    validator(value)


def validate_identity_number(value):
    """Validate an identity number."""
    validator = RegexValidator(
        regex=r"^\d{7,8}[-]?[0-9K]$",
        # regex=r'^\d{1,2}\.\d{3}\.\d{3}-[0-9K]$',
        message="Invalid identity number.",
        code="invalid_identity_number",
    )
    validator(value)


def validate_birth_date(value):
    """Validate that the person is at least 18 years old."""
    if (date.today() - value).days < 6570:  # 6570 days = 18 years
        raise ValidationError(
            "You must be at least 18 years old to register as a driver."
        )


def validate_food_image(image):
    """
    Validate that the uploaded image for a food item meets the required dimensions.
    """
    max_width = 600
    max_height = 600
    img = Image.open(image)
    width, height = img.size

    if width > max_width or height > max_height:
        raise ValidationError(
            f"Image dimensions should not exceed {max_width}x{max_height}px. "
            f"Uploaded image size is {width}x{height}px."
        )


@deconstructible
class FileSizeValidator:
    """
    Validator to check that a file's size does not exceed a specified limit.
    """

    message = "File size must be under %(limit)s. Current size is %(size)s."
    code = "invalid_size"

    def __init__(self, limit_mb, message=None, code=None):
        self.limit = limit_mb * 1024 * 1024

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        if value.size > self.limit:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    "limit": filesizeformat(self.limit),
                    "size": filesizeformat(value.size),
                },
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.limit == other.limit
            and self.message == other.message
            and self.code == other.code
        )


@deconstructible
class ImageSizeValidator:
    """
    Validator to ensure the image does not exceed a specified size.
    """

    message = "The image must have a maximum size of %(max_width)sx%(max_height)spx"
    code = "invalid_max_size"

    def __init__(self, max_width, max_height):
        if not isinstance(max_width, int) or not isinstance(max_height, int):
            raise TypeError("max_width and max_height must be integers")
        self.max_width = max_width
        self.max_height = max_height

    def __call__(self, image):
        img = Image.open(image)
        width, height = img.size
        if width > self.max_width or height > self.max_height:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    "max_width": self.max_width,
                    "max_height": self.max_width,
                },
            )


class DateRangeValidator(BaseValidator):
    """
    Validator that checks if the date is within a range of days.
    """

    message = "Date must be within {days} days from the current date."
    code = "invalid_date_range"

    def __init__(self, days=0, *args, **kwargs):
        self.days = days

    def compare(self, value, current_date_plus_days):
        return value <= current_date_plus_days

    def clean(self, x):
        return x

    def get_limit_value(self):
        return datetime.now() + timedelta(days=self.days)

    def __call__(self, value):
        if isinstance(value, datetime.date):
            value = datetime.combine(value, datetime.min.time())
        if not self.compare(value, self.get_limit_value()):
            raise ValidationError(self.message.format(days=self.days), code=self.code)
