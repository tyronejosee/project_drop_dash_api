"""Choices for Jobs App."""

from django.db.models import TextChoices


class Status(TextChoices):
    """Choices for applicant status."""

    PENDING = "pending", "Pending"
    REVIEWED = "reviewed", "Reviewed"
    ACCEPTED = "accepted", "Accepted"
    REJECTED = "rejected", "Rejected"
