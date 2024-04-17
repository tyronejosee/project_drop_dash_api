""""Validators for Drivers App."""

from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


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
