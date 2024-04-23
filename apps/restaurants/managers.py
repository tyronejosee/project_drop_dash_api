"""Managers for Restaurants App."""

from django.db import models


class RestaurantManager(models.Manager):
    """Manager for Restaurant model."""

    def get_all(self):
        """Get all available restaurants"""
        return self.filter(available=True)
