"""Managers for Blogs App."""

from datetime import timedelta
from django.db.models import Manager
from django.utils import timezone


class PostManager(Manager):
    """Manager for Post Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Return a queryset of available posts."""
        return self.get_queryset().filter(available=True)

    def get_featured(self):
        """Return a queryset of featured posts."""
        return self.get_available().filter(is_featured=True)

    def get_recent(self):
        """Return a queryset of recent posts created within the last 7 days."""
        seven_days_ago = timezone.now() - timedelta(days=7)
        return self.get_available().filter(created_at__gte=seven_days_ago)[:25]
