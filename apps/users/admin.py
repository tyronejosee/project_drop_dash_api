"""Admin for Users App."""

from django.contrib import admin

from .models import User
from .choices import Role


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin for User model."""

    list_per_page = 25
    list_display = [
        "username",
        "email",
        "role",
        "is_staff",
    ]
    list_display_links = [
        "username",
    ]
    search_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
    ]
    list_filter = [
        "is_staff",
        "is_superuser",
        "is_active",
    ]
    readonly_fields = [
        "pk",
    ]
    ordering = [
        "username",
    ]

    actions = [
        "assign_client",
        "assign_advertiser",
        "assign_driver",
        "assign_dispatcher",
        "assign_partner",
        "assign_support",
        "assign_marketing",
        "assign_operations",
        "assign_finance",
        "assign_administrator",
    ]

    @admin.action(description="Assign selected users as Client")
    def assign_client(modeladmin, request, queryset):
        queryset.update(role=Role.CLIENT, is_staff=False)

    @admin.action(description="Assign selected users as Advertiser")
    def assign_advertiser(modeladmin, request, queryset):
        queryset.update(role=Role.ADVERTISER, is_staff=False)

    @admin.action(description="Assign selected users as Driver")
    def assign_driver(modeladmin, request, queryset):
        queryset.update(role=Role.DRIVER, is_staff=False)

    @admin.action(description="Assign selected users as Dispatcher")
    def assign_dispatcher(modeladmin, request, queryset):
        queryset.update(role=Role.DISPATCHER, is_staff=False)

    @admin.action(description="Assign selected users as Partner")
    def assign_partner(modeladmin, request, queryset):
        queryset.update(role=Role.PARTNER, is_staff=False)

    @admin.action(description="Assign selected users as Support")
    def assign_support(modeladmin, request, queryset):
        queryset.update(role=Role.SUPPORT, is_staff=False)

    @admin.action(description="Assign selected users as Marketing")
    def assign_marketing(modeladmin, request, queryset):
        queryset.update(role=Role.MARKETING, is_staff=False)

    @admin.action(description="Assign selected users as Operations")
    def assign_operations(modeladmin, request, queryset):
        queryset.update(role=Role.OPERATIONS, is_staff=False)

    @admin.action(description="Assign selected users as Finance")
    def assign_finance(modeladmin, request, queryset):
        queryset.update(role=Role.FINANCE, is_staff=False)

    @admin.action(description="Assign selected users as Administrator")
    def assign_administrator(modeladmin, request, queryset):
        queryset.update(role=Role.ADMINISTRATOR, is_staff=True)
