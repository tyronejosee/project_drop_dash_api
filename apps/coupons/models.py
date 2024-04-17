"""Models for Coupons App."""

from django.db import models

from apps.utilities.models import BaseModel
from .managers import FixedCouponManager, PercentageCouponManager


class FixedCoupon(BaseModel):
    """Model definition for FixedCoupon (Entity)."""
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    quantity = models.PositiveIntegerField(default=50)
    is_active = models.BooleanField(default=True)

    objects = FixedCouponManager()

    class Meta:
        """Meta definition for FixedCoupon."""
        verbose_name = "fixed coupon"
        verbose_name_plural = "fixed coupons"

    def __str__(self):
        return self.name


class PercentageCoupon(BaseModel):
    """Model definition for PercentageCoupon (Entity)."""
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    quantity = models.PositiveIntegerField(default=50)
    is_active = models.BooleanField(default=True)

    objects = PercentageCouponManager()

    class Meta:
        """Meta definition for PercentageCoupon."""
        verbose_name = "percentage coupon"
        verbose_name_plural = "percentage coupons"

    def __str__(self):
        return self.name
