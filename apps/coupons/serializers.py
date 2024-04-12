"""Serializers for Coupons App."""

from rest_framework.serializers import ModelSerializer

from .models import FixedDiscountCoupon, PercentageDiscountCoupon


class FixedDiscountCouponSerializer(ModelSerializer):
    """Serializer for FixedDiscountCoupon model."""

    class Meta:
        """Meta definition for FixedDiscountCouponSerializer."""
        model = FixedDiscountCoupon
        fields = [
            "id",
            "name",
            "code",
            "discount_price",
            "start_date",
            "end_date",
            "quantity",
            "is_active",
            "created_at",
            "updated_at"
        ]


class PercentageDiscountCouponSerializer(ModelSerializer):
    """Serializer for PercentageDiscountCoupon model."""

    class Meta:
        """Meta definition for PercentageDiscountCouponSerializer."""
        model = PercentageDiscountCoupon
        fields = [
            "id",
            "name",
            "code",
            "discount_percentage",
            "start_date",
            "end_date",
            "quantity",
            "is_active",
            "created_at",
            "updated_at"
        ]
