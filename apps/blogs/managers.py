"""Managers for Blogs App."""

from datetime import timedelta
from django.db.models import Q
from django.utils import timezone

from apps.utilities.managers import BaseManager


class TagManager(BaseManager):
    """Manager for Tag Model."""


class PostManager(BaseManager):
    """Manager for Post Model."""

    def get_featured(self):
        """Return a queryset of featured posts."""
        return self.get_available().filter(is_featured=True)

    def get_recent(self):
        """Return a queryset of recent posts created within the last 7 days."""
        seven_days_ago = timezone.now() - timedelta(days=7)
        return self.get_available().filter(created_at__gte=seven_days_ago)[:25]

    def search_by_term(self, search_term):
        """Filter promotions based on a search term."""
        return self.get_available().filter(
            Q(title__icontains=search_term)
            | Q(content__icontains=search_term)
            | Q(tags__name__icontains=search_term)
        )


class PostReportManager(BaseManager):
    """Manager for PostReport Model."""
