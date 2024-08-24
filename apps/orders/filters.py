"""Filters for Orders App."""

from django_filters import rest_framework as filters

from .models import Order
from .choices import OrderStatusChoices, PaymentMethodChoices


class OrderFilter(filters.FilterSet):
    """Filter for Order model."""

    status = filters.ChoiceFilter(
        field_name="status",
        choices=OrderStatusChoices.choices,
        label="Filter by order status, ex `/?status=not_processed`",
    )
    payment_method = filters.ChoiceFilter(
        field_name="payment_method",
        choices=PaymentMethodChoices.choices,
        label="Filter by payment method, ex `/?payment_method=credit_card`",
    )
    is_payment = filters.BooleanFilter(
        field_name="is_payment",
        label="Filter by payment status, ex `/?is_payment=true`",
    )
    is_valid = filters.BooleanFilter(
        field_name="is_valid",
        label="Filter by validation status, ex `/?is_valid=true`",
    )
    ordering = filters.OrderingFilter(
        fields=(
            ("created_at", "newest"),
            ("created_at", "oldest"),
            ("amount", "highest_amount"),
            ("amount", "lowest_amount"),
        ),
        field_labels={
            "created_at": "Newest",
            "-created_at": "Oldest",
            "amount": "Highest Amount",
            "-amount": "Lowest Amount",
        },
        label="Order by Newest Oldest, Highest Amount, Lowest Amount, ex `/?ordering=newest`",
    )

    class Meta:
        model = Order
        fields = [
            "status",
            "payment_method",
            "is_payment",
            "is_valid",
            "ordering",
        ]


class UserOrderFilter(filters.FilterSet):
    """Filter for Order model (For Users)."""

    is_payment = filters.BooleanFilter(
        field_name="is_payment",
        label="Filter by payment status, ex `/?is_payment=true`",
    )
    ordering = filters.OrderingFilter(
        fields=(
            ("created_at", "newest"),
            ("created_at", "oldest"),
        ),
        field_labels={
            "created_at": "Newest",
            "-created_at": "Oldest",
        },
        label="Order by Newest or Oldest, ex `/?ordering=newest`",
    )

    class Meta:
        model = Order
        fields = [
            "is_payment",
            "ordering",
        ]
