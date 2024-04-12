"""Models for Coupons App."""

from django.db import models

from apps.utilities.models import BaseModel


class FixedDiscountCoupon(BaseModel):
    """Model definition for FixedDiscountCoupon (Entity)."""
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    discount_price = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    quantity = models.PositiveIntegerField(default=50)
    is_active = models.BooleanField(default=True)
    # TODO: add is_active logic

    def __str__(self):
        return self.name


class PercentageDiscountCoupon(BaseModel):
    """Model definition for PercentageDiscountCoupon (Entity)."""
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    quantity = models.PositiveIntegerField(default=50)
    is_active = models.BooleanField(default=True)
    # TODO: add is_active logic

    def __str__(self):
        return self.name
