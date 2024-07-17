"""Admin for Orders App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(BaseAdmin):
    """Admin for Order model."""

    search_fields = ["transaction", "user"]
    list_display = ["transaction", "is_available", "created_at", "status"]
    list_filter = ["status"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["created_at"]


@admin.register(OrderItem)
class OrderItemAdmin(BaseAdmin):
    """Admin for OrderItem model."""

    search_fields = ["order", "food"]
    list_display = ["order", "food", "created_at", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "price", "subtotal", "created_at", "updated_at"]
    ordering = ["created_at"]
