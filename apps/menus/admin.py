"""Admin for Menus App."""

from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Admin config for Menu model."""
    search_fields = ["user", "restaurant"]
    list_display = [
        "restaurant", "available", "created_at", "updated_at"
    ]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Admin config for MenuItem model."""
    search_fields = ["menu", "food"]
    list_display = ["menu", "available", "created_at", "updated_at"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]
