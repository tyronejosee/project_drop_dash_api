"""Serializers for Orders App."""

from rest_framework.serializers import (
    ModelSerializer, ReadOnlyField, StringRelatedField,
    ChoiceField, ValidationError)

from apps.foods.serializers import FoodMiniSerializer
from .models import Order, OrderItem
from .choices import OrderStatus


class UUIDField(ReadOnlyField):
    def to_representation(self, value):
        return str(value)


class OrderSerializer(ModelSerializer):
    """Serializer for Order model."""
    user = UUIDField()
    transaction = UUIDField(read_only=True)
    comune = StringRelatedField()
    region = StringRelatedField()
    status = ChoiceField(choices=OrderStatus.choices)

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

    def validate_status(self, value):
        """Validate that status is one of the choices."""
        if value not in dict(OrderStatus.choices):
            raise ValidationError("Invalid status")
        return value


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
