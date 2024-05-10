"""Admin for Blogs App."""

from django.contrib import admin

from .models import Tag, Post


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin for Tag model."""
    search_fields = ["name",]
    list_display = ["name", "available",]
    list_editable = ["available"]
    list_filter = ["available",]
    list_per_page = 25
    readonly_fields = ["pk", "slug", "created_at", "updated_at",]
    ordering = ["name",]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin for Post model."""
    search_fields = ["title", "author"]
    list_display = ["title", "author", "available",]
    list_editable = ["available"]
    list_filter = ["tags", "available",]
    list_per_page = 25
    readonly_fields = ["pk", "slug", "created_at", "updated_at",]
    ordering = ["title",]
