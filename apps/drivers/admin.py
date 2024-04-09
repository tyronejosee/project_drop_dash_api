"""Admin for Drivers App."""

from django.contrib import admin

from .models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    """Admin config for Driver model."""
    search_fields = ["user",]
    list_display = ["user", "available", "created_at", "updated_at"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]
