"""Managers for Promotions App."""

from django.db.models import Q

from apps.utilities.managers import BaseManager


class PromotionManager(BaseManager):
    """Manager for Promotion model."""

    # TODO: fix manager, add new manager

    def get_available(self):
        return self.get_queryset().select_related("creator").filter(available=True)

    def get_search(self, search_term):
        return self.get_available().filter(
            Q(name__icontains=search_term) | Q(conditions__icontains=search_term)
        )


class FixedCouponManager(BaseManager):
    """Manager for FixedCoupon model."""

    # TODO: fix manager, add new manager

    def get_available(self):
        return self.filter(available=True, is_active=True)

    def get_by_code(self, code):
        return self.get_available().filter(code=code).first()


class PercentageCouponManager(BaseManager):
    """Manager for PercentageCoupon model."""

    # TODO: fix manager, add new manager

    def get_available(self):
        return self.filter(available=True, is_active=True)

    def get_by_code(self, code):
        return self.get_available().filter(code=code).first()
