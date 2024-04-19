"""Choices for Orders App."""

from django.db import models


class OrderStatus(models.TextChoices):
    """Choices for status of a order."""
    NOT_PROCESSED = "not_processed", "Not Processed"
    PROCESSED = "processed", "Processed"
    SHIPPING = "shipping", "Shipping"
    DELIVERED = "delivered", "Delivered"
    CANCELLED = "cancelled", "Cancelled"
