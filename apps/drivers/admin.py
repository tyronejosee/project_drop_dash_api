"""Admin for Drivers App."""

from django.contrib import admin

from .models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    """Admin for Driver model."""
    search_fields = ["user",]
    list_display = ["user", "created_at", "updated_at", "available"]
    list_editable = ["available"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]
