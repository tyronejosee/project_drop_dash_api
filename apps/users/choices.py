"""Choices for Contents App."""

from django.db.models import TextChoices


class Role(TextChoices):
    """Choices for user roles."""

    CLIENT = "client", "Client"
    ADVERTISER = "advertiser", "Advertiser"
    DRIVER = "driver", "Driver"
    DISPATCHER = "dispatcher", "Dispatcher"
    PARTNER = "partner", "Partner"
    SUPPORT = "support", "Support"
    MARKETING = "marketing", "Marketing"
    OPERATIONS = "operations", "Operations"
    FINANCE = "finance", "Finance"
    ADMINISTRATOR = "administrator", "Administrator"
