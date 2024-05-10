"""Serializers for Coupons App."""

from rest_framework.serializers import ModelSerializer

from .models import FixedCoupon, PercentageCoupon


class FixedCouponSerializer(ModelSerializer):
    """Serializer for FixedCoupon model."""

    class Meta:
        model = FixedCoupon
        fields = [
            "id",
            "name",
            "code",
            "discount_price",
            "start_date",
            "end_date",
            "quantity",
            "is_active"
        ]


class PercentageCouponSerializer(ModelSerializer):
    """Serializer for PercentageCoupon model."""

    class Meta:
        model = PercentageCoupon
        fields = [
            "id",
            "name",
            "code",
            "discount_percentage",
            "start_date",
            "end_date",
            "quantity",
            "is_active"
        ]
