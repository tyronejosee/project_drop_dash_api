"""Managers for Orders App."""

from apps.utilities.managers import BaseManager


class OrderManager(BaseManager):
    """Manager for Order Model."""

    def get_by_status(self, status):
        """Get orders by status"""
        return self.get_available().filter(status=status)

    def get_by_user(self, user):
        """Get orders by status"""
        return self.get_available().filter(user_id=user)


class OrderItemManager(BaseManager):
    """Manager for OrderItem Model."""
