"""Admin for Promotions App."""

from django.contrib import admin

from .models import Promotion


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
