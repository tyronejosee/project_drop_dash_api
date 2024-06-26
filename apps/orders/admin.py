"""Admin for Orders App."""

from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin for Order model."""

    list_per_page = 25
    search_fields = [
        "transaction",
        "user",
    ]
    list_display = [
        "transaction",
        "available",
        "created_at",
        "status",
    ]
    list_filter = [
        "status",
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


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Admin for OrderItem model."""

    list_per_page = 25
    search_fields = [
        "order",
        "food",
    ]
    list_display = [
        "order",
        "food",
        "created_at",
        "available",
    ]
    list_editable = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "price",
        "subtotal",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "created_at",
    ]
