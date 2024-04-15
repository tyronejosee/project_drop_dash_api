"""Serializers for Orders App."""

from rest_framework.serializers import ModelSerializer

from apps.locations.serializers import ComuneSerializer, RegionSerializer
from .models import Order


class OrderSerializer(ModelSerializer):
    """Serializer for Order model."""
    comune = ComuneSerializer(read_only=True)
    region = RegionSerializer(read_only=True)

    class Meta:
        """Meta definition for RestaurantSerializer."""
        model = Order
        fields = [
            "id",
            "transaction",
            "user",
            "address",
            "comune",
            "region",
            "phone",
            "note",
            "status",
            "payment_method",
            "payment_status",
            "estimated_delivery_time",
            "actual_delivery_time",
            "created_at",
            "updated_at"
        ]
