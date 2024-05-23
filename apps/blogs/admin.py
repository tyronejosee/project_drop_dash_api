"""Admin for Blogs App."""

from django.contrib import admin

from .models import Tag, Post, PostReport
from .choices import Status


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin for Tag model."""

    list_per_page = 25
    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "available",
    ]
    list_editable = [
        "available",
    ]
    list_filter = [
        "available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "name",
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin for Post model."""

    list_per_page = 25
    search_fields = [
        "title",
        "author",
    ]
    list_display = [
        "title",
        "author",
        "available",
    ]
    list_editable = [
        "available",
    ]
    list_filter = [
        "tags",
        "available",
    ]
    readonly_fields = [
        "pk",
        "slug",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "title",
    ]


@admin.register(PostReport)
class PostReportAdmin(admin.ModelAdmin):
    """Admin for PostReport model."""

    list_per_page = 25
    search_fields = [
        "user",
    ]
    list_display = [
        "user",
        "priority",
        "status",
    ]
    list_editable = [
        "status",
    ]
    list_filter = [
        "priority",
        "status",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "-priority",
    ]

    actions = [
        "make_approved",
        "make_rejected",
        "make_archived",
    ]

    @admin.action(description="Mark selected reports as Approved")
    def make_approved(modeladmin, request, queryset):
        queryset.update(status=Status.APPROVED)

    @admin.action(description="Mark selected reports as Rejected")
    def make_rejected(modeladmin, request, queryset):
        queryset.update(status=Status.REJECTED)

    @admin.action(description="Mark selected reports as Rejected")
    def make_archived(modeladmin, request, queryset):
        queryset.update(status=Status.ARCHIVED)
