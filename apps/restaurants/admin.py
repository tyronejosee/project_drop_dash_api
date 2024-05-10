"""Admin for Restaurants App."""

from django.contrib import admin

from .models import Restaurant, Category


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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin config for Category model."""
    search_fields = ["name", "restaurant"]
    list_display = ["name", "restaurant", "available",]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["name",]
