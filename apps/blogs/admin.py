"""Admin for Blogs App."""

from django.contrib import admin

from apps.utilities.admin import BaseAdmin
from .models import Tag, Post, PostReport
from .choices import StatusChoices


class TagInline(admin.TabularInline):
    model = Post.tags.through
    extra = 1


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

    search_fields = ["title", "author"]
    list_display = ["title", "author", "is_available"]
    list_editable = ["is_available"]
    list_filter = ["tags", "is_available"]
    readonly_fields = ["pk", "slug", "created_at", "updated_at"]
    ordering = ["title"]
    inlines = [TagInline]


@admin.register(PostReport)
class PostReportAdmin(BaseAdmin):
    """Admin for PostReport model."""

    search_fields = ["user"]
    list_display = ["user", "priority", "status"]
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
