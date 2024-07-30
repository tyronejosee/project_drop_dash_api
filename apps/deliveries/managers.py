"""Managers for Deliveries App."""

from apps.utilities.managers import BaseManager


class DeliveryManager(BaseManager):
    """Manager for Delivery Model."""


class FailedDeliveryManager(BaseManager):
    """Manager for FailedDelivery Model."""
