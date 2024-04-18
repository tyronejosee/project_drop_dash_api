"""Validators for Coupons App."""

from django.core.exceptions import ValidationError


def validate_discount_price(value):
    if value < 5000:  # $5.000 CLP
        raise ValidationError(
            "The minimum discount must be $5.000 CLP.",
            params={"value": value},
        )
    if value > 20000:  # $20.000 CLP
        raise ValidationError(
            "The maximum discount must be $20.000 CLP.",
            params={"value": value},
        )
