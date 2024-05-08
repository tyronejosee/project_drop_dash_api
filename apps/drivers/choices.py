"""Choices for Drivers App."""

from django.db import models


class Status(models.TextChoices):
    """Choices for status of a driver."""
    BRONCE = "Bronce"
    SILVER = "Silver"
    DIAMOND = "Diamond"
    ALERT = "Alert"
