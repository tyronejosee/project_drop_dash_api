"""Filters for Drivers App."""

from django_filters import rest_framework as filters

from .models import Driver
from .choices import VehicleChoices, StatusChoices


class DriverFilter(filters.FilterSet):
    """Filter for Driver model."""

    vehicle_type = filters.ChoiceFilter(
        field_name="vehicle_type",
        choices=VehicleChoices.choices,
        label="Filter by vehicle type, ex `/?vehicle_type=automobile`",
    )
    status = filters.ChoiceFilter(
        field_name="status",
        choices=StatusChoices.choices,
        label="Filter by driver status, ex `/?status=silver`",
    )
    is_verified = filters.BooleanFilter(
        field_name="is_verified",
        label="Filter by verified availability, ex `/?is_verified=true`",
    )
    is_active = filters.BooleanFilter(
        field_name="is_active",
        label="Filter by active availability, ex `/?is_active=true`",
    )

    class Meta:
        model = Driver
        fields = [
            "vehicle_type",
            "status",
            "is_verified",
            "is_active",
        ]
