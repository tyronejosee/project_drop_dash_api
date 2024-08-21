"""Managers for Home App."""

from apps.utilities.managers import BaseManager


class CompanyManager(BaseManager):
    """Manager for Company model."""


class PageManager(BaseManager):
    """Manager for Page model."""

    def get_list(self):
        return self.get_available().only("id", "name")

    def get_detail(self):
        return self.get_available().defer("is_available")


class KeywordManager(BaseManager):
    """Manager for Keyword model."""
