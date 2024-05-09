"""Managers for Orders App."""

from django.db import models


class OrderManager(models.Manager):
    """Manager for Order Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available orders"""
        return self.get_queryset().filter(available=True)

    def get_unavailable(self):
        """Get all unavailable orders"""
        return self.get_queryset().filter(available=False)

    def get_by_status(self, status):
        """Get orders by status"""
        return self.get_available().filter(status=status)

    def get_by_user(self, user):
        """Get orders by status"""
        return self.get_available().filter(user=user)


class OrderItemManager(models.Manager):
    """Manager for OrderItem Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available orders items"""
        return self.get_queryset().filter(available=True)

    def get_unavailable(self):
        """Get all unavailable orders items"""
        return self.get_queryset().filter(available=False)
