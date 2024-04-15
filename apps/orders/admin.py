"""Admin for Orders App."""

from django.contrib import admin

from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin config for Order model."""
    search_fields = ["transaction", "user"]
    list_display = ["transaction", "available", "created_at", "status"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["created_at",]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Admin config for OrderItem model."""
    search_fields = ["order", "food"]
    list_display = ["order", "food", "created_at", "available"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["created_at",]
