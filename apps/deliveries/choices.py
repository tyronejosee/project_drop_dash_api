"""Choices for Deliveries App."""

from django.db.models import TextChoices


class Status(TextChoices):

    IN_PROGRESS = "progress", "In Progress"
    COMPLETED = "completed", "Completed"
    CANCELLED = "cancelled", "Cancelled"
