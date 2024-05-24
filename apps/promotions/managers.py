"""Managers for Promotions App."""

from django.db.models import Manager, Q


class PromotionManager(Manager):
    """Manager for Promotion model."""

    def get_queryset(self):
        # Default queryset
        return super().get_queryset()

    def get_available(self):
        return self.get_queryset().select_related("creator").filter(available=True)

    def get_unavailable(self):
        return self.get_queryset().filter(available=False)

    def get_search(self, search_term):
        return self.get_available().filter(
            Q(name__icontains=search_term) | Q(conditions__icontains=search_term)
        )


class FixedCouponManager(Manager):
    """Manager for FixedCoupon model."""

    def get_available(self):
        return self.filter(available=True, is_active=True)

    def get_by_code(self, code):
        return self.get_available().filter(code=code).first()


class PercentageCouponManager(Manager):
    """Manager for PercentageCoupon model."""

    def get_available(self):
        return self.filter(available=True, is_active=True)

    def get_by_code(self, code):
        return self.get_available().filter(code=code).first()
