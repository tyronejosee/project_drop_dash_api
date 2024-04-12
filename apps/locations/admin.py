"""Admin for Locations App."""

from django.contrib import admin

from .models import Region, Comune


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    """Admin config for Region model."""
    search_fields = ["name",]
    list_display = ["name", "available", "created_at", "updated_at"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]


@admin.register(Comune)
class ComuneAdmin(admin.ModelAdmin):
    """Admin config for Comune model."""
    search_fields = ["name", "region"]
    list_display = ["name", "region", "available", "created_at", "updated_at"]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["pk",]
