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


class CategoryManager(models.Manager):
    """Manager for Category model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available categories."""
        return self.get_queryset().filter(available=True)

    def get_by_restaurant(self, restaurant):
        """Get all categories for a specific restaurant."""
        return self.get_available().filter(
            restaurant=restaurant)


class FoodManager(models.Manager):
    """Manager for Food Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available foods."""
        return self.get_queryset().filter(available=True)

    def get_foods_by_restaurant(self, restaurant):
        """Get all foods for a specific restaurant."""
        return self.get_available().filter(
            restaurant=restaurant).select_related("restaurant", "category")

    def get_featured_foods(self):
        """Get all featured foods."""
        return self.get_available().filter(
            is_featured=True).select_related("restaurant", "category")
