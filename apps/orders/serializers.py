"""Serializers for Orders App."""

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Order, OrderItem


class OrderItemReadSerializer(ModelSerializer):
    """Serializer for OrderItem model (List/update)."""
    food = SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = [
            "food",
            "quantity",
            "price",
            "subtotal"
        ]

    def get_food(self, obj):
        return str(obj.food)


class OrderReadSerializer(ModelSerializer):
    """Serializer for Order model (List/retrieve)."""
    foods = OrderItemReadSerializer(source='orderitem_set', many=True)

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
            "payment_method",
            "foods"
        ]
