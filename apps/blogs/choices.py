"""Choices for Orders App."""

from django.db.models import TextChoices


class Priority(TextChoices):
    """Choices for report priorities."""

    LOW = "low", "Low"
    MEDIUM = "medium", "Medium"
    HIGH = "high", "High"
    URGENT = "urgent", "Urgent"


class Status(TextChoices):
    """Choices for report status."""

    PENDING = "pending", "Pending"
    APPROVED = "approved", "Approved"
    REJECTED = "rejected", "Rejected"
    ARCHIVED = "archived", "Archived"
