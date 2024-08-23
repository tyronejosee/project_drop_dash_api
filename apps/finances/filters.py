"""Filters for Finaces App."""

from django_filters import rest_framework as filters

from apps.utilities.filters import BaseFilter
from .models import Revenue
from .choices import TransactionTypeChoices


class RevenueFilter(BaseFilter):
    """Filter for Revenue model."""

    amount = filters.RangeFilter(
        field_name="amount",
        label="Filter by amount, ex `/?amount_min=10&amount_max=100`",
    )
    transaction_type = filters.ChoiceFilter(
        field_name="transaction_type",
        choices=TransactionTypeChoices.choices,
        label="Filter by transaction type, ex `/?transaction_type=restaurant_commission`",
    )

    class Meta:
        model = Revenue
        fields = [
            "amount",
            "transaction_type",
        ]
