"""Admin for Deliveries App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Delivery


@admin.register(Delivery)
class DeliveryAdmin(BaseAdmin):
    """Admin for Delivery model."""

    search_fields = ["order_id", "driver_id"]
    list_display = ["pk", "order_id", "is_completed", "is_available"]
    list_filter = ["status"]
    list_editable = ["is_completed", "is_available"]
    readonly_fields = ["pk", "picked_up_at", "delivered_at", "created_at", "updated_at"]
    autocomplete_fields = ["order_id", "driver_id"]
