"""Filters for Jobs App."""

from django_filters import rest_framework as filters

from apps.utilities.filters import BaseFilter
from .models import Worker, Applicant
from .choices import ContractTypeChoices, StatusChoices


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
        label="Filter by position (position name), ex `/?position=Data Analyst`",
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


class ApplicantFilter(BaseFilter):
    """Filter for Applicant model."""

    position = filters.CharFilter(
        field_name="position_id__position",
        lookup_expr="icontains",
        label="Filter by position (position name), ex `/?position=Data Analyst`",
    )
    submitted_at = filters.DateTimeFilter(
        field_name="submitted_at",
        lookup_expr="exact",
        label="Filter by submission date (exact match), ex `/?submitted_at=2024-01-01T22:30:00`",
    )
    submitted_at__gte = filters.DateTimeFilter(
        field_name="submitted_at",
        lookup_expr="gte",
        label="Filter by submission date (greater than or equal), ex `/?submitted_at__gte=2024-01-01`",
    )
    submitted_at__lte = filters.DateTimeFilter(
        field_name="submitted_at",
        lookup_expr="lte",
        label="Filter by submission date (less than or equal), ex `/?submitted_at__lte=2024-01-01`",
    )
    status = filters.ChoiceFilter(
        field_name="status",
        choices=StatusChoices.choices,
        label="Filter by status, ex `/?status=accepted`",
    )

    class Meta:
        model = Applicant
        fields = [
            "position",
            "submitted_at",
            "status",
        ]
