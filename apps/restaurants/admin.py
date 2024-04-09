"""Admin for Restaurants App."""

from django.contrib import admin

from .models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    """Admin config for Restaurant model."""
    # search_fields = ["name",]
    # list_display = ["available",]
    # list_per_page = 25
    # readonly_fields = ["pk", "slug", "created_at", "updated_at",]
    # ordering = ["name",]
