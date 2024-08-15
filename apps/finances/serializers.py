"""Serializers for Finances App."""

from rest_framework import serializers

from apps.utilities.mixins import ReadOnlyFieldsMixin
from .models import Revenue


class RevenueReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Revenue model (List/retrieve)."""

    order_id = serializers.StringRelatedField()
    driver_id = serializers.StringRelatedField()
    restaurant_id = serializers.StringRelatedField()
    transaction_type = serializers.CharField(source="get_transaction_type_display")

    class Meta:
        model = Revenue
        fields = [
            "id",
            "order_id",
            "driver_id",
            "restaurant_id",
            "amount",
            "transaction_type",
            "updated_at",
            "created_at",
        ]


class RevenueWriteSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Revenue model (Create/Update)."""

    class Meta:
        model = Revenue
        fields = [
            "order_id",
            "driver_id",
            "restaurant_id",
            "amount",
            "transaction_type",
        ]

    # ! TODO: Add transaction type validation
