"""Choices for Users App."""

from django.db.models import TextChoices


class RoleChoices(TextChoices):

    CLIENT = "client", "Client"
    ADVERTISER = "advertiser", "Advertiser"
    DRIVER = "driver", "Driver"
    DISPATCHER = "dispatcher", "Dispatcher"
    PARTNER = "partner", "Partner"
    SUPPORT = "support", "Support"
    MARKETING = "marketing", "Marketing"
    OPERATIONS = "operations", "Operations"
    FINANCE = "finance", "Finance"
    HUMAN_RESOURCES = "human_resources", "Human Resources"
    ADMINISTRATOR = "administrator", "Administrator"
