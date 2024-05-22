"""Admin for Reviews App."""

from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin for Review model."""

    list_per_page = 25
    search_fields = [
        "user",
        "object_id",
    ]
    list_display = [
        "user",
        "content_type",
        "content_object",
        "rating",
        "available",
    ]
    list_editable = [
        "available",
    ]
    list_filter = [
        "rating",
        "content_type",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
