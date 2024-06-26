"""Choices for Drivers App."""

from django.db.models import TextChoices


class Vehicle(TextChoices):

    AUTOMOBILE = "automobile", "Automobile"
    MOTORCYCLE = "motorcycle", "Motorcycle"
    BICYCLE = "bicycle", "Bicycle"


class Status(TextChoices):

    BRONCE = "bronce", "Bronce"
    SILVER = "silver", "Silver"
    DIAMOND = "diamond", "Diamond"
    ALERT = "alert", "Alert"


class ResourceType(TextChoices):

    BACKPACKS = "backpacks", "Backpacks"
    UNIFORMS = "uniforms", "Uniforms"
    OTHERS = "others", "Others"


class RequestStatus(TextChoices):

    PENDING = "pending", "Pending"
    APPROVED = "approved", "Approved"
    REJECTED = "rejected", "Rejected"
