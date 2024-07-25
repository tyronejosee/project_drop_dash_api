"""Filters for Jobs App."""

from django_filters import rest_framework as filters

from apps.utilities.filters import BaseFilter
from .models import Worker
from .choices import ContractTypeChoices


class WorkerFilter(BaseFilter):
    """Filter for Worker model."""

    user = filters.CharFilter(
        field_name="user_id__username",
        lookup_expr="icontains",
        label="Filter by user (username), ex `/?user=randomuser`",
    )
    city = filters.CharFilter(
        field_name="city_id__name",
        lookup_expr="icontains",
        label="Filter by city name, ex `/?city=New York`",
    )
    state = filters.CharFilter(
        field_name="state_id__name",
        lookup_expr="icontains",
        label="Filter by city name, ex `/?state=California`",
    )
    country = filters.CharFilter(
        field_name="country_id__name",
        lookup_expr="icontains",
        label="Filter by country name, ex `/?country_name=USA`",
    )
    position = filters.CharFilter(
        field_name="position_id__position",
        lookup_expr="icontains",
        label="Filter by position (position), ex `/?position=Data Analyst`",
    )
    contract_type = filters.ChoiceFilter(
        field_name="contract_type",
        choices=ContractTypeChoices.choices,
        label="Filter by contract type, ex `/?contract_type=fixed_term`",
    )

    class Meta:
        model = Worker
        fields = [
            "user",
            "city",
            "state",
            "country",
            "position",
            "contract_type",
        ]
