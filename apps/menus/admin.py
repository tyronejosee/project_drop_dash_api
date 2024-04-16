"""Admin for Menus App."""

from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    """Admin config for Menu model."""
    search_fields = ["restaurant", "food"]
    list_display = [
        "restaurant", "available", "created_at", "updated_at"
    ]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]
