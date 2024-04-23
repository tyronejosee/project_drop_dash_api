"""Managers for Categories App."""

from django.db import models


class CategoryManager(models.Manager):
    """Manager for Category model."""

    def get_all(self):
        """Return default queryset."""
        return self.filter(available=True).prefetch_related("restaurant")
