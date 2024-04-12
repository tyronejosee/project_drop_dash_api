"""Admin for Categories App."""

from django.contrib import admin

from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin config for Category model."""
    search_fields = ["name",]
    list_display = ["name", "available",]
    list_per_page = 25
    readonly_fields = ["pk", "slug", "created_at", "updated_at",]
    ordering = ["name",]
