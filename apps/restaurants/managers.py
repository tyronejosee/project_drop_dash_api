"""Managers for Restaurants App."""

from django.db.models import Q

from apps.utilities.managers import BaseManager


class RestaurantManager(BaseManager):
    """Manager for Restaurant model."""

    # TODO: fix manager

    def get_available(self):
        """Get all available restaurants"""
        return self.filter(available=True, is_verified=True)

    def get_search(self, search_term):
        """Filter restaurants based on a search term."""
        return self.get_available().filter(
            Q(name__icontains=search_term)
            | Q(description__icontains=search_term)
            | Q(address__icontains=search_term)
        )


class CategoryManager(BaseManager):
    """Manager for Category model."""

    def get_by_restaurant(self, restaurant):
        """Get all categories for a specific restaurant."""
        return self.get_available().filter(restaurant=restaurant)


class FoodManager(BaseManager):
    """Manager for Food Model."""

    def get_foods_by_restaurant(self, restaurant):
        """Get all foods for a specific restaurant."""
        return (
            self.get_available()
            .filter(restaurant=restaurant)
            .select_related("restaurant", "category")
        )

    def get_featured_foods(self):
        """Get all featured foods."""
        return (
            self.get_available()
            .filter(is_featured=True)
            .select_related("restaurant", "category")
        )
