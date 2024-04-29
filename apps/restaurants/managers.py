"""Managers for Restaurants App."""

from django.db import models


class RestaurantManager(models.Manager):
    """Manager for Restaurant model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available restaurants"""
        return self.get_queryset().filter(available=True)

    def get_unavailable(self):
        """Get all unavailable restaurants"""
        return self.get_queryset().filter(available=False)
