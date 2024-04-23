"""Admin for Restaurants App."""

from django.contrib import admin

from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Admin config for Restaurant model."""
    search_fields = ["name", "user"]
    list_display = ["name", "available",]
    list_editable = ["available"]
    list_filter = ["specialty", "is_open"]
    list_per_page = 25
    readonly_fields = ["pk", "slug", "is_open", "created_at", "updated_at",]
    ordering = ["name",]
