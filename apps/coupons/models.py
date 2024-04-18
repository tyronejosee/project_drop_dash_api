"""Models for Coupons App."""

from datetime import timedelta
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

from apps.utilities.models import BaseModel
from .managers import FixedCouponManager, PercentageCouponManager
from .validators import validate_discount_price


class FixedCoupon(BaseModel):
    """Model definition for FixedCoupon (Entity)."""
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=36, unique=True, blank=True)
    discount_price = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[validate_discount_price])
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now() + timedelta(days=30))
    quantity = models.PositiveIntegerField(default=50)
    is_active = models.BooleanField(default=True)

    objects = FixedCouponManager()

    class Meta:
        """Meta definition for FixedCoupon."""
        verbose_name = "fixed coupon"
        verbose_name_plural = "fixed coupons"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate a code based on the pk
        if not self.code:
            self.code = self.pk
        super().save(*args, **kwargs)


class PercentageCoupon(BaseModel):
    """Model definition for PercentageCoupon (Entity)."""
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=36, unique=True, blank=True)
    discount_percentage = models.IntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(25)])
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now() + timedelta(days=30))
    quantity = models.PositiveIntegerField(default=50)
    is_active = models.BooleanField(default=True)

    objects = PercentageCouponManager()

    class Meta:
        """Meta definition for PercentageCoupon."""
        verbose_name = "percentage coupon"
        verbose_name_plural = "percentage coupons"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Generate a code based on the pk
        if not self.code:
            self.code = self.pk
        super().save(*args, **kwargs)
