"""Managers for Coupons App."""

from django.db import models


class FixedCouponManager(models.Manager):
    """Manager for FixedCoupon model."""

    def get_all(self):
        """Return default queryset."""
        return self.filter(available=True, is_active=True)


class PercentageCouponManager(models.Manager):
    """Manager for PercentageCoupon model."""

    def get_all(self):
        """Return default queryset."""
        return self.filter(available=True, is_active=True)
