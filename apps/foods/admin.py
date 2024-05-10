"""Admin for Foods App."""

from django.contrib import admin

from .models import Food


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    """Admin for Driver model."""
    search_fields = ["name", "restaurant"]
    list_display = [
        "name", "restaurant", "available", "created_at", "updated_at"
    ]
    list_editable = ["available",]
    list_filter = ["restaurant", "category"]
    list_per_page = 25
    readonly_fields = ["pk", "sale_price", "created_at", "updated_at",]
    autocomplete_fields = ["restaurant", "category"]
    ordering = ["pk",]
