"""Serializers for Orders App."""

from rest_framework import serializers

from apps.utilities.mixins import ReadOnlyFieldsMixin
from apps.users.serializers import UserMinimalSerializer
from apps.restaurants.serializers import RestaurantMinimalSerializer
from .models import Order, OrderItem


class OrderReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Order model (List/retrieve)."""

    user_id = UserMinimalSerializer()
    city_id = serializers.StringRelatedField()
    state_id = serializers.StringRelatedField()
    country_id = serializers.StringRelatedField()
    restaurant_id = RestaurantMinimalSerializer()
    status = serializers.CharField(source="get_status_display")
    payment_method = serializers.CharField(source="get_payment_method_display")

    class Meta:
        model = Order
        fields = [
            "id",
            "user_id",
            "shipping_name",
            "shipping_phone",
            "shipping_time",
            "shipping_price",
            "transaction",
            "address_1",
            "address_2",
            "city_id",
            "state_id",
            "country_id",
            "note",
            "zip_code",
            "restaurant_id",
            "amount",
            "status",
            "payment_method",
            "updated_at",
            "created_at",
        ]


class OrderWriteSerializer(serializers.ModelSerializer):
    """Serializer for Order model (Create/update)."""

    class Meta:
        model = Order
        fields = [
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
            "restaurant_id",
            # "amount",
            # "status",
            "payment_method",
        ]


class OrderMinimalSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Order model (Minimal)."""

    restaurant_id = serializers.StringRelatedField()
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Order
        fields = [
            "id",
            "shipping_name",
            "transaction",
            "restaurant_id",
            "amount",
            "status",
            "updated_at",
            "created_at",
        ]


class OrderItemReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for OrderItem model (List/update)."""

    food_id = serializers.SerializerMethodField()

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
