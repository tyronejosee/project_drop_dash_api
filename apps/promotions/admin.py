"""Admin for Promotions App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Promotion, FixedCoupon, PercentageCoupon


@admin.register(Promotion)
class PromotionAdmin(BaseAdmin):
    """Admin for Order model."""

    search_fields = ["name", "user"]
    list_display = ["name", "created_at", "is_available"]
    list_filter = ["is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["created_at"]


@admin.register(FixedCoupon)
class FixedCouponAdmin(BaseAdmin):
    """Admin for FixedCoupon model."""

    search_fields = ["name", "code"]
    list_display = ["name", "discount_price", "is_active", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]


@admin.register(PercentageCoupon)
class PercentageCouponAdmin(BaseAdmin):
    """Admin for PercentageCoupon model."""

    search_fields = ["name", "code"]
    list_display = ["name", "discount_percentage", "is_active", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]
