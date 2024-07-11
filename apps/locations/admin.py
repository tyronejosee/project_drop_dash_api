"""Admin for Locations App."""

from django.contrib import admin

from apps.utilities.models import BaseModel
from .models import Country, State, City


@admin.register(Country)
class CountryAdmin(BaseModel):
    """Admin for Country model."""

    search_fields = ["name"]
    list_display = ["name", "is_available", "created_at"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]


@admin.register(State)
class StateAdmin(BaseModel):
    """Admin for State model."""

    search_fields = ["name", "country"]
    list_display = ["name", "is_available", "created_at", "updated_at"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]


@admin.register(City)
class CityAdmin(BaseModel):
    """Admin for City model."""

    search_fields = ["name", "state"]
    list_display = ["name", "is_available", "created_at", "updated_at"]
    readonly_fields = ["pk", "created_at", "updated_at"]
    ordering = ["pk"]
