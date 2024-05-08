"""Managers for Categories App."""

from django.db import models


class CategoryManager(models.Manager):
    """Manager for Category model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_all(self):
        """Return default queryset."""
        return self.get_queryset().filter(
            available=True).prefetch_related("restaurant")
