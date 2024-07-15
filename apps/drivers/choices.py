"""Choices for Drivers App."""

from django.db.models import TextChoices


class VehicleChoices(TextChoices):

    AUTOMOBILE = "automobile", "Automobile"
    MOTORCYCLE = "motorcycle", "Motorcycle"
    BICYCLE = "bicycle", "Bicycle"


class StatusChoices(TextChoices):

    BRONCE = "bronce", "Bronce"
    SILVER = "silver", "Silver"
    DIAMOND = "diamond", "Diamond"
    ALERT = "alert", "Alert"


class ResourceTypeChoices(TextChoices):

    BACKPACKS = "backpacks", "Backpacks"
    UNIFORMS = "uniforms", "Uniforms"
    OTHERS = "others", "Others"


class RequestStatusChoices(TextChoices):

    PENDING = "pending", "Pending"
    APPROVED = "approved", "Approved"
    REJECTED = "rejected", "Rejected"
