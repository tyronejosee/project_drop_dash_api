"""Filters for Animes App."""

from django_filters import rest_framework as filters

from apps.utilitiess.filters import BaseFilter
from .models import Restaurant
from .choices import SpecialtyChoices


class RestaurantFilter(BaseFilter):
    """Filter for Restaurant model."""

    name = filters.CharFilter(
        field_name="name",
        lookup_expr="icontains",
        label="Filter by restaurant name, ex `/?name=mcdonals`",
    )
    # ! TODO: Remove or merge with viewset's search_fields
    specialty = filters.ChoiceFilter(
        field_name="specialty",
        choices=SpecialtyChoices.choices,
        label="Filter by specialty, ex `/?specialty=italian`",
    )
    city = filters.CharFilter(
        field_name="city__name",
        lookup_expr="icontains",
        label="Filter by city name, ex `/?city=newyork`",
    )
    state = filters.CharFilter(
        field_name="state__name",
        lookup_expr="icontains",
        label="Filter by state name, ex `/?state=california`",
    )
    country = filters.CharFilter(
        field_name="country__name",
        lookup_expr="icontains",
        label="Filter by country name, ex `/?country=usa`",
    )
    is_open = filters.BooleanFilter(
        field_name="is_open",
        label="Filter by open status, ex `/?is_open=true`",
    )

    class Meta:
        model = Restaurant
        fields = [
            "name",
            "specialty",
            "city",
            "state",
            "country",
            "is_verified",
            "is_open",
        ]
