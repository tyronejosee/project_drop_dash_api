"""Admin for Foods App."""

from django.contrib import admin

from .models import Food


@admin.register(Food)
class DriverAdmin(admin.ModelAdmin):
    """Admin config for Driver model."""
    search_fields = ["name", "restaurant"]
    list_display = [
        "restaurant", "name", "available", "created_at", "updated_at"
    ]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]
