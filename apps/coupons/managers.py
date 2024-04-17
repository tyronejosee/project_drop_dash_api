"""Managers for Coupons App."""

from django.db import models


class FixedCouponManager(models.Manager):
    """Manager for FixedCoupon model."""

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, available=True)


class PercentageCouponManager(models.Manager):
    """Manager for PercentageCoupon model."""

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, available=True)
