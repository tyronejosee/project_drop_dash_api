""""Validators for Drivers App."""

from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible


def validate_phone(value):
    """Validate a phone number according to the Chilean format."""
    validator = RegexValidator(
        regex=r'^\+56\d{9}$',
        message="Invalid phone number.",
        code="invalid_name"
    )
    validator(value)


def validate_birth_date(value):
    """Validate that the person is at least 18 years old."""
    if (date.today() - value).days < 6570:  # 6570 days = 18 years
        raise ValidationError(
            "You must be at least 18 years old to register as a driver."
        )


@deconstructible
class FileSizeValidator:
    message = "File size must be under %(limit)s. Current size is %(size)s."
    code = "invalid_size"

    # TODO: Add translation if the project grows

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
