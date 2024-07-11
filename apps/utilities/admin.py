"""Admin for Utils App."""

from django.contrib import admin


class BaseAdmin(admin.ModelAdmin):
    """Base Admin."""

    list_per_page = 25
    date_hierarchy = "created_at"
    actions = ["soft_delete", "restore_items"]

    @admin.action(description="Soft delete selected items")
    def soft_delete(self, request, queryset):
        """Action to perform soft delete by setting is_available to False."""
        queryset.update(is_available=False)

    @admin.action(description="Restore selected items")
    def restore_items(self, request, queryset):
        """Action to restore items by setting is_available to True."""
        queryset.update(is_available=True)
