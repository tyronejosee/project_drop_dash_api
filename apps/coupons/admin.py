"""Admin for Coupons App."""

from django.contrib import admin

from .models import FixedDiscountCoupon, PercentageDiscountCoupon


@admin.register(FixedDiscountCoupon)
class FixedDiscountCouponAdmin(admin.ModelAdmin):
    """Admin config for FixedDiscountCoupon model."""
    search_fields = ["name", "code"]
    list_display = ["name", "discount_price", "is_active"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(PercentageDiscountCoupon)
class PercentageDiscountCouponAdmin(admin.ModelAdmin):
    """Admin config for PercentageDiscountCoupon model."""
    search_fields = ["name", "code"]
    list_display = ["name", "discount_percentage", "is_active"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]
