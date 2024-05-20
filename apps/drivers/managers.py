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

    def get_drivers_by_city(self, city_id):
        """Return a queryset of drivers in a specific city."""
        return self.get_available().filter(city=city_id)


class ResourceManager(models.Manager):
    """Manager for Resource Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Return a queryset of available resources."""
        return self.get_queryset().filter(available=True)
