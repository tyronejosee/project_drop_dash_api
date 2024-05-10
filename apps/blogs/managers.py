"""Managers for Blogs App."""

from django.db.models import Manager


class PostManager(Manager):
    """Manager for Post Model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Return a queryset of available posts."""
        return self.get_queryset().filter(available=True)
