"""Admin for Orders App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Order, OrderItem, OrderRating, OrderReport


@admin.register(Order)
class OrderAdmin(BaseAdmin):
    """Admin for Order model."""

    search_fields = ["transaction", "user_id"]
    list_display = ["transaction", "is_available", "created_at", "status"]
    list_filter = ["status"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "transaction", "created_at", "updated_at"]
    ordering = ["created_at"]


@admin.register(OrderItem)
class OrderItemAdmin(BaseAdmin):
    """Admin for OrderItem model."""

    search_fields = ["order_id", "food_id"]
    list_display = ["order_id", "food_id", "created_at", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "price", "subtotal", "created_at", "updated_at"]
    ordering = ["created_at"]


@admin.register(OrderRating)
class OrderRatingAdmin(BaseAdmin):
    """Admin for OrderRating model."""

    search_fields = ["order_id", "user_id"]
    list_display = ["pk", "order_id"]
    list_filter = ["rating"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    autocomplete_fields = ["order_id", "user_id"]


@admin.register(OrderReport)
class OrderReportAdmin(BaseAdmin):
    """Admin for OrderReport model."""

    search_fields = ["order_id", "user_id"]
    list_display = ["pk", "order_id", "user_id"]
    list_filter = ["status", "is_resolved"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    autocomplete_fields = ["order_id", "user_id"]
