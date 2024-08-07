"""Choices for Orders App."""

from django.db import models


class OrderStatusChoices(models.TextChoices):

    NOT_PROCESSED = "not_processed", "Not Processed"
    PROCESSED = "processed", "Processed"
    SHIPPING = "shipping", "Shipping"
    DELIVERED = "delivered", "Delivered"
    CANCELLED = "cancelled", "Cancelled"


class ReportStatusChoices(models.TextChoices):

    PENDING = "pending", "Pending"
    RESOLVED = "resolved", "Resolved"
    REJECTED = "rejected", "Rejected"
    CLOSED = "closed", "Closed"
