"""Serializers for Orders App."""

from rest_framework.serializers import (
    ModelSerializer, ReadOnlyField, StringRelatedField,
    ChoiceField, ValidationError)

from apps.foods.serializers import FoodMiniSerializer
from apps.payments.choices import PaymentMethod
from .models import Order, OrderItem
from .choices import OrderStatus


class UUIDField(ReadOnlyField):
    def to_representation(self, value):
        return str(value)


class OrderWriteSerializer(ModelSerializer):
    """Serializer for Order model (Create/update)."""

    class Meta:
        model = Order
        fields = [
            "id",
            "transaction",
            "restaurant",
            "address",
            "comune",
            "region",
            "phone",
            "note",
            "status",
            "payment_method"
        ]
        read_only_fields = ["user", "transaction", "status"]

    def validate_status(self, value):
        """Validate that status is one of the choices."""
        if value not in dict(OrderStatus.choices):
            raise ValidationError("Invalid status")
        return value

    def validate_payment_method(self, value):
        """Validate that payment_method is one of the choices."""
        if value not in dict(PaymentMethod.choices):
            raise ValidationError("Invalid payment method")
        return value


class OrderReadSerializer(ModelSerializer):
    """Serializer for Order model (List/retrieve)."""
    user = UUIDField()
    transaction = UUIDField(read_only=True)
    comune = StringRelatedField()
    region = StringRelatedField()
    status = ChoiceField(choices=OrderStatus.choices)
    payment_method = ChoiceField(choices=PaymentMethod.choices)

    class Meta:
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

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order",
            "food",
            "quantity",
            "price",
            "subtotal"
        ]

    def to_representation(self, instance):
        # Overridden method to include serializers for foreign keys
        data = super().to_representation(instance)
        data["food"] = FoodMiniSerializer(instance.food).data
        return data
