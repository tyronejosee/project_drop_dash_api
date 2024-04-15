"""Choices for Orders App."""

from django.db import models


class OrderStatus(models.TextChoices):
    """Pending."""
    NOT_PROCESSED = "not_processed", "Not Processed"
    PROCESSED = "processed", "Processed"
    SHIPPING = "shipping", "Shipping"
    DELIVERED = "delivered", "Delivered"
    CANCELLED = "cancelled", "Cancelled"
