"""Admin for Drivers App."""

from django.contrib import admin

from .models import Driver, Resource


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    """Admin for Driver model."""

    list_per_page = 25
    search_fields = [
        "user",
    ]
    list_display = [
        "user",
        "created_at",
        "updated_at",
        "available",
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
        "pk",
    ]


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    """Admin for Resource model."""

    list_per_page = 25
    search_fields = [
        "driver",
        "status",
    ]
    list_display = [
        "driver",
        "status",
        "available",
    ]
    list_editable = [
        "status",
        "available",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "driver",
    ]
