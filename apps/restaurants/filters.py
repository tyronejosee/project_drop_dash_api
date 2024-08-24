"""Filters for Animes App."""

from django_filters import rest_framework as filters

from apps.utilities.filters import BaseFilter
from .models import Restaurant, Category, Food
from .choices import SpecialtyChoices


class RestaurantFilter(BaseFilter):
    """Filter for Restaurant model."""

    specialty = filters.ChoiceFilter(
        field_name="specialty",
        choices=SpecialtyChoices.choices,
        label="Filter by specialty, ex `/?specialty=italian`",
    )
    city = filters.CharFilter(
        field_name="city_id__name",
        lookup_expr="icontains",
        label="Filter by city name, ex `/?city=newyork`",
    )
    state = filters.CharFilter(
        field_name="state_id__name",
        lookup_expr="icontains",
        label="Filter by state name, ex `/?state=california`",
    )
    country = filters.CharFilter(
        field_name="country_id__name",
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


class FoodFilter(filters.FilterSet):
    """Filter for Food model."""

    min_price = filters.NumberFilter(
        field_name="price",
        lookup_expr="gte",
        label="Filter by minimum price, ex `/?min_price=10.00`",
    )
    max_price = filters.NumberFilter(
        field_name="price",
        lookup_expr="lte",
        label="Filter by maximum price, ex `/?max_price=50.00`",
    )
    is_featured = filters.BooleanFilter(
        field_name="is_featured",
        label="Filter by featured status, ex `/?is_featured=True`",
    )
    category = filters.ModelChoiceFilter(
        queryset=Category.objects.get_available(),
        field_name="category_id",
        label="Filter by category, ex `/?category=1`",
    )

    class Meta:
        model = Food
        fields = [
            "min_price",
            "max_price",
            "is_featured",
            "category",
        ]
