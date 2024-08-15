"""Admin for Finances App."""

from django.contrib import admin
from apps.utilities.admin import BaseAdmin

from .models import Revenue


@admin.register(Revenue)
class RevenueAdmin(BaseAdmin):
    """Admin for Revenue model."""

    search_fields = ["order_id", "driver_id", "restaurant_id"]
    list_display = [
        "order_id",
        "driver_id",
        "restaurant_id",
        "transaction_type",
        "amount",
    ]
    list_filter = ["transaction_type"]
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]
