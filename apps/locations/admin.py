"""Admin for Locations App."""

from django.contrib import admin

from .models import Country, State, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """Admin for Country model."""

    list_per_page = 25
    search_fields = [
        "name",
    ]
    list_display = [
        "name",
        "available",
        "created_at",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "pk",
    ]


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """Admin for State model."""

    list_per_page = 25
    search_fields = [
        "name",
        "country",
    ]
    list_display = [
        "name",
        "available",
        "created_at",
        "updated_at",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "pk",
    ]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """Admin for City model."""

    list_per_page = 25
    search_fields = [
        "name",
        "state",
    ]
    list_display = [
        "name",
        "available",
        "created_at",
        "updated_at",
    ]
    readonly_fields = [
        "pk",
        "created_at",
        "updated_at",
    ]
    ordering = [
        "pk",
    ]
