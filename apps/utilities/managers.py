"""Managers for Utilities App."""

from django.db import models


class BaseManager(models.Manager):
    """Base Manager."""

    def get_available(self):
        return self.filter(is_available=True)

    def get_unavailable(self):
        return self.filter(is_available=False)
