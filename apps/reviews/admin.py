"""Admin for Reviews App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Review


@admin.register(Review)
class ReviewAdmin(BaseAdmin):
    """Admin for Review model."""

    search_fields = ["user_id", "object_id"]
    list_display = [
        "user_id",
        "content_type",
        "content_object",
        "rating",
        "is_available",
    ]
    list_editable = ["is_available"]
    list_filter = ["rating", "content_type"]
    readonly_fields = ["pk", "created_at", "updated_at"]
