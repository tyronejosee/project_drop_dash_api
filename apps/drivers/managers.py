"""Managers for Drivers App."""

from django.db import models


class DriverManager(models.Manager):
    """Manager for Driver Model."""

    def get_available_drivers(self):
        """Return a queryset of available drivers."""
        return self.filter(available=True)

    def get_drivers_by_status(self, status):
        """Return a queryset of drivers with the specified status."""
        return self.filter(status=status)

    def get_drivers_by_region(self, region_id):
        """Return a queryset of drivers in a specific region."""
        return self.filter(region=region_id)
