"""Managers for Locations App."""

from apps.utilities.managers import BaseManager


class CountryManager(BaseManager):
    """Manager for Country Model."""


class StateManager(BaseManager):
    """Manager for State Model."""

    def get_list(self):
        return self.get_available().only("id", "name")

    def get_detail(self):
        return self.get_available().select_related("country_id")


class CityManager(BaseManager):
    """Manager for City Model."""

    def get_list(self):
        return self.get_available().only("id", "name")

    def get_detail(self):
        return self.get_available().select_related("state_id")
