"""Admin for Drivers App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Driver, Resource


@admin.register(Driver)
class DriverAdmin(BaseAdmin):
    """Admin for Driver model."""

    search_fields = ["user_id"]
    list_display = ["user_id", "created_at", "updated_at", "is_available"]
    list_editable = ["is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]


@admin.register(Resource)
class ResourceAdmin(BaseAdmin):
    """Admin for Resource model."""

    search_fields = ["driver_id", "status"]
    list_display = ["driver_id", "status", "is_available"]
    list_editable = ["status", "is_available"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["driver_id"]
