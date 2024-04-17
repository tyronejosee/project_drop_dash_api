"""Admin for Coupons App."""

from django.contrib import admin

from .models import FixedCoupon, PercentageCoupon


@admin.register(FixedCoupon)
class FixedCouponAdmin(admin.ModelAdmin):
    """Admin config for FixedCoupon model."""
    search_fields = ["name", "code"]
    list_display = ["name", "discount_price", "is_active"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(PercentageCoupon)
class PercentageCouponAdmin(admin.ModelAdmin):
    """Admin config for PercentageCoupon model."""
    search_fields = ["name", "code"]
    list_display = ["name", "discount_percentage", "is_active"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]
