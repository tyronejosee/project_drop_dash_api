"""Choices for Deliveries App."""

from django.db.models import TextChoices


class StatusChoices(TextChoices):

    PENDING = "pending", "Pending"
    ASSIGNED = "assigned", "Assigned"
    PICKED_UP = "picked_up", "Picked Up"
    DELIVERED = "delivered", "Delivered"
    FAILED = "failed", "Failed"
