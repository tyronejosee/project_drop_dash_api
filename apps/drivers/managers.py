"""Managers for Drivers App."""

from django.db import models


class DriverManager(models.Manager):
    """Manager for Driver Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Return a queryset of available drivers."""
        return self.get_queryset().filter(available=True)

    def get_drivers_by_status(self, status):
        """Return a queryset of drivers with the specified status."""
        return self.get_available().filter(status=status)

    def get_drivers_by_region(self, region_id):
        """Return a queryset of drivers in a specific region."""
        return self.get_available().filter(region=region_id)
