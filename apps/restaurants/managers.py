"""Managers for Restaurants App."""

from django.db.models import Manager, Q


class RestaurantManager(Manager):
    """Manager for Restaurant model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available restaurants"""
        return self.get_queryset().filter(available=True, is_verified=True)

    def get_unavailable(self):
        """Get all unavailable restaurants"""
        return self.get_queryset().filter(available=False)

    def get_search(self, search_term):
        """Filter restaurants based on a search term."""
        return self.get_available().filter(
            Q(name__icontains=search_term)
            | Q(description__icontains=search_term)
            | Q(address__icontains=search_term)
        )


class CategoryManager(Manager):
    """Manager for Category model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available categories."""
        return self.get_queryset().filter(available=True)

    def get_by_restaurant(self, restaurant):
        """Get all categories for a specific restaurant."""
        return self.get_available().filter(restaurant=restaurant)


class FoodManager(Manager):
    """Manager for Food Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Get all available foods."""
        return self.get_queryset().filter(available=True)

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
