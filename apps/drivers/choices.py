"""Choices for Drivers App."""

from django.db.models import TextChoices


class Status(TextChoices):
    """Choices for driver status."""

    BRONCE = "bronce", "Bronce"
    SILVER = "silver", "Silver"
    DIAMOND = "diamond", "Diamond"
    ALERT = "alert", "Alert"
