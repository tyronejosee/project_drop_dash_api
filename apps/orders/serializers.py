"""Serializers for Orders App."""

from rest_framework.serializers import ModelSerializer, ReadOnlyField

from apps.locations.serializers import (
    ComuneListSerializer, RegionListSerializer)
from apps.foods.serializers import FoodMiniSerializer
from .models import Order, OrderItem


class UUIDField(ReadOnlyField):
    def to_representation(self, value):
        return str(value)


class OrderSerializer(ModelSerializer):
    """Serializer for Order model."""
    user = UUIDField()
    transaction = UUIDField(read_only=True)
    comune = ComuneListSerializer()
    region = RegionListSerializer()

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
            "payment_method"
        ]


class OrderItemSerializer(ModelSerializer):
    """Serializer for OrderItem model."""
    food = FoodMiniSerializer()

    class Meta:
        """Meta definition for OrderItemSerializer."""
        model = OrderItem
        fields = [
            "id",
            "order",
            "food",
            "quantity",
            "price",
            "subtotal"
        ]
