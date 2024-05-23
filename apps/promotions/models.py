"""Models for Promotions App."""

from django.conf import settings
from django.db import models
from django.core.validators import (
    FileExtensionValidator,
    MinValueValidator,
    MaxValueValidator,
)

from apps.utilities.validators import FileSizeValidator, DateRangeValidator
from apps.utilities.models import BaseModel
from apps.utilities.paths import image_path
from .validators import validate_discount_price
from .managers import PromotionManager, FixedCouponManager, PercentageCouponManager

User = settings.AUTH_USER_MODEL


class Promotion(BaseModel):
    """Model definition for Promotion."""

    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    conditions = models.TextField()
    start_date = models.DateField(DateRangeValidator(days=90))
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to=image_path,
        validators=[
            FileExtensionValidator(allowed_extensions=["webp"]),
            FileSizeValidator(limit_mb=1),
        ],
    )

    objects = PromotionManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "promotion"
        verbose_name_plural = "promotions"

    def __str__(self):
        return str(self.name)


class CouponBase(BaseModel):
    """Model definition for CouponBase."""

    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=36, unique=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["pk"]
        abstract = True

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # Generate a code based on the pk
        if not self.code:
            self.code = self.pk
        super().save(*args, **kwargs)


class FixedCoupon(CouponBase):
    """Model definition for FixedCoupon."""

    discount_price = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[validate_discount_price]
    )

    objects = FixedCouponManager()

    class Meta:
        verbose_name = "fixed coupon"
        verbose_name_plural = "fixed coupons"


class PercentageCoupon(CouponBase):
    """Model definition for PercentageCoupon (Entity)."""

    discount_percentage = models.IntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(25)]
    )

    objects = PercentageCouponManager()

    class Meta:
        verbose_name = "percentage coupon"
        verbose_name_plural = "percentage coupons"
