"""Choices for Deliveries App."""

from django.db.models import TextChoices


class Status(TextChoices):
    """Choices for deliveries status."""

    IN_PROGRESS = "progress", "In Progress"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"
