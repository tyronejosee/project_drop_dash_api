"""Managers for Drivers App."""

from apps.utilities.managers import BaseManager


class DriverManager(BaseManager):
    """Manager for Driver Model."""

    def get_drivers_by_status(self, status):
        """Return a queryset of drivers with the specified status."""
        return self.get_available().filter(status=status)

    def get_drivers_by_city(self, city_id):
        """Return a queryset of drivers in a specific city."""
        return self.get_available().filter(city_id=city_id)


class ResourceManager(BaseManager):
    """Manager for Resource Model."""
