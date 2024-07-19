"""Filters for Animes App."""

from django_filters import rest_framework as filters

from apps.utilities.filters import BaseFilter
from .models import Promotion, CouponBase, FixedCoupon, PercentageCoupon


class PromotionFilter(BaseFilter):
    """Filter for Promotion model."""

    start_date = filters.DateFilter(
        lookup_expr="exact",
        label="Filter by start date, ex `/?start_date=2024-01-01`",
    )
    start_date__gte = filters.DateFilter(
        field_name="start_date",
        lookup_expr="gte",
        label="Filter by start date (greater than or equal), ex `/?start_date__gte=2024-01-01`",
    )
    start_date__lte = filters.DateFilter(
        field_name="start_date",
        lookup_expr="lte",
        label="Filter by start date (less than or equal), ex `/?start_date__lte=2024-01-01`",
    )
    end_date = filters.DateFilter(
        lookup_expr="exact",
        label="Filter by end date, ex `/?end_date=2024-01-01`",
    )
    end_date__gte = filters.DateFilter(
        field_name="end_date",
        lookup_expr="gte",
        label="Filter by end date (greater than or equal), ex `/?end_date__gte=2024-01-01`",
    )
    end_date__lte = filters.DateFilter(
        field_name="end_date",
        lookup_expr="lte",
        label="Filter by end date (less than or equal), ex `/?end_date__lte=2024-01-01`",
    )

    class Meta:
        model = Promotion
        fields = [
            "name",
            "start_date",
            "end_date",
        ]


class CouponBaseFilter(BaseFilter):
    """Filter for Coupons (Base)."""

    code = filters.CharFilter(
        lookup_expr="icontains",
        label="Filter by coupon code, ex `/?code=ABCD1234`",
    )
    start_date = filters.DateFilter(
        lookup_expr="exact",
        label="Filter by start date, ex `/?start_date=2024-01-01`",
    )
    start_date__gte = filters.DateFilter(
        field_name="start_date",
        lookup_expr="gte",
        label="Filter by start date (greater than or equal), ex `/?start_date__gte=2024-01-01`",
    )
    start_date__lte = filters.DateFilter(
        field_name="start_date",
        lookup_expr="lte",
        label="Filter by start date (less than or equal), ex `/?start_date__lte=2024-01-01`",
    )
    end_date = filters.DateFilter(
        lookup_expr="exact",
        label="Filter by end date, ex `/?end_date=2024-01-01`",
    )
    end_date__gte = filters.DateFilter(
        field_name="end_date",
        lookup_expr="gte",
        label="Filter by end date (greater than or equal), ex `/?end_date__gte=2024-01-01`",
    )
    end_date__lte = filters.DateFilter(
        field_name="end_date",
        lookup_expr="lte",
        label="Filter by end date (less than or equal), ex `/?end_date__lte=2024-01-01`",
    )
    quantity = filters.NumberFilter(
        lookup_expr="exact",
        label="Filter by quantity, ex `/?quantity=10`",
    )
    quantity__gte = filters.NumberFilter(
        field_name="quantity",
        lookup_expr="gte",
        label="Filter by quantity (greater than or equal), ex `/?quantity__gte=10`",
    )
    quantity__lte = filters.NumberFilter(
        field_name="quantity",
        lookup_expr="lte",
        label="Filter by quantity (less than or equal), ex `/?quantity__lte=10`",
    )

    class Meta:
        model = CouponBase
        fields = [
            "code",
            "start_date",
            "end_date",
            "quantity",
        ]


class FixedCouponFilter(CouponBaseFilter):
    """Filter for FixedCoupon model."""

    discount_price = filters.NumberFilter(
        lookup_expr="exact",
        label="Filter by discount price, ex `/?discount_price=9.99`",
    )
    discount_price__gte = filters.NumberFilter(
        field_name="discount_price",
        lookup_expr="gte",
        label="Filter by discount price (greater than or equal), ex `/?discount_price__gte=9.99`",
    )
    discount_price__lte = filters.NumberFilter(
        field_name="discount_price",
        lookup_expr="lte",
        label="Filter by discount price (less than or equal), ex `/?discount_price__lte=9.99`",
    )

    class Meta:
        model = FixedCoupon
        fields = CouponBaseFilter.Meta.fields + ["discount_price"]


class PercentageCouponFilter(CouponBaseFilter):
    """Filter for PercentageCoupon model."""

    discount_percentage = filters.NumberFilter(
        lookup_expr="exact",
        label="Filter by discount percentage, ex `/?discount_percentage=10`",
    )
    discount_percentage__gte = filters.NumberFilter(
        field_name="discount_percentage",
        lookup_expr="gte",
        label="Filter by discount percentage (greater than or equal), ex `/?discount_percentage__gte=10`",
    )
    discount_percentage__lte = filters.NumberFilter(
        field_name="discount_percentage",
        lookup_expr="lte",
        label="Filter by discount percentage (less than or equal), ex `/?discount_percentage__lte=10`",
    )

    class Meta:
        model = PercentageCoupon
        fields = CouponBaseFilter.Meta.fields + ["discount_percentage"]
