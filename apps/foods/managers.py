"""Managers for Foods App."""

from django.db import models


class FoodManager(models.Manager):
    """Manager for Food Model."""

    def get_all(self):
        """Get all available foods"""
        return self.filter(available=True)

    def get_foods_by_restaurant(self, restaurant):
        """Get all foods for a specific restaurant."""
        return self.filter(restaurant=restaurant).select_related(
            "restaurant", "category")

    def get_featured_foods(self):
        """Get all featured foods."""
        return self.filter(is_featured=True).select_related(
            "restaurant", "category")
