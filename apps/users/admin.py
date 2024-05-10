"""Admin for Users App."""

from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin for User model."""
    list_display = ["username", "email", "is_staff", "is_superuser"]
    list_display_links = ["username"]
    search_fields = ["username", "email", "first_name", "last_name"]
    list_filter = ["is_staff", "is_superuser", "is_active"]
    list_per_page = 25
    readonly_fields = ["pk",]
    ordering = ["username",]
