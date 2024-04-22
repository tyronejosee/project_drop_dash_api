""""Validators for Drivers App."""

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from datetime import date


# TODO: Remove validator.py, error in migrations dependencies

validate_phone = RegexValidator(
    regex=r'^\+569\d{8}$',
    message="Invalid phone number."
)


def validate_birth_date(value):
    """Validate that the person is at least 18 years old."""
    if (date.today() - value).days < 6570:  # 6570 days = 18 years
        raise ValidationError(
            "You must be at least 18 years old to register as a driver."
        )
