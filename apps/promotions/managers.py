"""Managers for Promotions App."""

from django.db.models import Q

from apps.utilities.managers import BaseManager


class PromotionManager(BaseManager):
    """Manager for Promotion model."""

    def get_active(self):
        return (
            self.get_available()
            .filter(is_active=True)
            .select_related(
                "creator_id",
            ),
        )

    def get_search(self, search_term):
        return self.get_available().filter(
            Q(name__icontains=search_term) | Q(conditions__icontains=search_term)
        )


class FixedCouponManager(BaseManager):
    """Manager for FixedCoupon model."""

    def get_active(self):
        return self.get_available().filter(is_active=True)

    def get_by_code(self, code):
        return self.get_available().filter(code=code).first()


class PercentageCouponManager(BaseManager):
    """Manager for PercentageCoupon model."""

    def get_active(self):
        return self.get_available().filter(is_active=True)

    def get_by_code(self, code):
        return self.get_available().filter(code=code).first()
