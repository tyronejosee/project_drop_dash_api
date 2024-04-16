"""Admin for Categories App."""

from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin config for Category model."""
    search_fields = ["name", "restaurant"]
    list_display = ["name", "restaurant", "available",]
    list_per_page = 25
    readonly_fields = ["pk", "created_at", "updated_at",]
    ordering = ["name",]
