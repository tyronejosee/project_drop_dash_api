"""Admin for Reviews App."""

from django.contrib import admin

from apps.utilities.models import BaseModel
from .models import Review


@admin.register(Review)
class ReviewAdmin(BaseModel):
    """Admin for Review model."""

    search_fields = ["user", "object_id"]
    list_display = ["user", "content_type", "content_object", "rating", "is_available"]
    list_editable = ["is_available"]
    list_filter = ["rating", "content_type"]
    readonly_fields = ["pk", "created_at", "updated_at"]
