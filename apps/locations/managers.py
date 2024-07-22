"""Managers for Locations App."""

from apps.utilities.managers import BaseManager


class CountryManager(BaseManager):
    """Manager for Country Model."""


class StateManager(BaseManager):
    """Manager for State Model."""


class CityManager(BaseManager):
    """Manager for City Model."""
