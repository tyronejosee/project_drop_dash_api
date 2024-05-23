"""Managers for Promotions App."""

from django.db.models import Manager, Q


class PromotionManager(Manager):
    """Manager for Promotion model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        """Return a queryset of available promotions."""
        return self.get_queryset().select_related("creator").filter(available=True)

    def get_unavailable(self):
        """Return a queryset of unavailable promotions."""
        return self.get_queryset().filter(available=False)

    def get_search(self, search_term):
        """Filter promotions based on a search term."""
        return self.get_available().filter(
            Q(name__icontains=search_term) | Q(conditions__icontains=search_term)
        )


class FixedCouponManager(Manager):
    """Manager for FixedCoupon model."""

    def get_all(self):
        """Return default queryset."""
        return self.filter(available=True, is_active=True)


class PercentageCouponManager(Manager):
    """Manager for PercentageCoupon model."""

    def get_all(self):
        """Return default queryset."""
        return self.filter(available=True, is_active=True)
