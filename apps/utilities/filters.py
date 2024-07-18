"""Filters for Utilities App."""

from django_filters import rest_framework as filters

from .choices import SortChoices


class BaseFilter(filters.FilterSet):
    """Base filter class with common filters."""

    sort = filters.ChoiceFilter(
        choices=SortChoices.choices,
        method="filter_by_order",
        label="Search query sort direction, ex `/?=sort=asc`",
    )

    def filter_by_order(self, queryset, name, value):
        order_by = self.data.get("order_by", "name")
        if value == "asc":
            return queryset.order_by(order_by)
        elif value == "desc":
            return queryset.order_by("-" + order_by)
        return queryset
