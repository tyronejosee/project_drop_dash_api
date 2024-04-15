"""Choices for Drivers App."""

from django.db import models


class Status(models.TextChoices):
    """Choices for status of a driver."""
    BRONCE = "bronce", "Bronce"
    SILVER = "silver", "Silver"
    DIAMOND = "diamond", "Diamond"
    ALERT = "alert", "Alert"
