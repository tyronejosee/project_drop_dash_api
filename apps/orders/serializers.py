"""Serializers for Orders App."""

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Order, OrderItem


class OrderItemReadSerializer(ModelSerializer):
    """Serializer for OrderItem model (List/update)."""

    food_id = SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = [
            "food_id",
            "quantity",
            "price",
            "subtotal",
        ]

    def get_food_id(self, obj):
        return str(obj.food_id)


class OrderReadSerializer(ModelSerializer):
    """Serializer for Order model (List/retrieve)."""

    foods = OrderItemReadSerializer(source="orderitem_set", many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "transaction",
            "user_id",
            "shipping_name",
            "shipping_phone",
            "shipping_time",
            "shipping_price",
            "address_1",
            "address_2",
            "city_id",
            "state_id",
            "country_id",
            "note",
            "zip_code",
            "status",
            "amount",
            "payment_method",
            "foods",
        ]
