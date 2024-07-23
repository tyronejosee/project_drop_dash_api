"""Admin for Blogs App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Tag, Post, PostReport
from .choices import StatusChoices


@admin.register(Tag)
class TagAdmin(BaseAdmin):
    """Admin for Tag model."""

    search_fields = ["name"]
    list_display = ["name", "is_available"]
    list_editable = ["is_available"]
    list_filter = ["is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]
    ordering = ["name"]


@admin.register(Post)
class PostAdmin(BaseAdmin):
    """Admin for Post model."""

    search_fields = ["title", "author_id"]
    list_display = ["title", "author_id", "is_available"]
    list_editable = ["is_available"]
    list_filter = ["tags", "is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]
    ordering = ["title"]


@admin.register(PostReport)
class PostReportAdmin(BaseAdmin):
    """Admin for PostReport model."""

    search_fields = ["user_id"]
    list_display = ["user_id", "priority", "status"]
    list_editable = ["status"]
    list_filter = ["priority", "status"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["-priority"]

    actions = ["make_approved", "make_rejected", "make_archived"]

    @admin.action(description="Mark selected reports as Approved")
    def make_approved(modeladmin, request, queryset):
        queryset.update(status=StatusChoices.APPROVED)

    @admin.action(description="Mark selected reports as Rejected")
    def make_rejected(modeladmin, request, queryset):
        queryset.update(status=StatusChoices.REJECTED)

    @admin.action(description="Mark selected reports as Rejected")
    def make_archived(modeladmin, request, queryset):
        queryset.update(status=StatusChoices.ARCHIVED)
