"""Managers for Promotions App."""

from django.db.models import Manager


class PromotionManager(Manager):
    """Manager for Promotion model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Return a queryset of available promotions."""
        return self.get_queryset().filter(available=True)

    def get_unavailable(self):
        """Return a queryset of unavailable promotions."""
        return self.get_queryset().filter(available=False)
