"""Admin for Promotions App."""

from django.contrib import admin

from .models import Promotion, FixedCoupon, PercentageCoupon


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    """Admin for Order model."""

    list_per_page = 25
    search_fields = [
        "name",
        "user",
    ]
    list_display = [
        "name",
        "created_at",
        "available",
    ]
    list_filter = [
        "available",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "created_at",
    ]


@admin.register(FixedCoupon)
class FixedCouponAdmin(admin.ModelAdmin):
    """Admin for FixedCoupon model."""

    list_per_page = 25
    search_fields = [
        "name",
        "code",
    ]
    list_display = [
        "name",
        "discount_price",
        "is_active",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "pk",
    ]


@admin.register(PercentageCoupon)
class PercentageCouponAdmin(admin.ModelAdmin):
    """Admin for PercentageCoupon model."""

    list_per_page = 25
    search_fields = [
        "name",
        "code",
    ]
    list_display = [
        "name",
        "discount_percentage",
        "is_active",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "pk",
    ]
