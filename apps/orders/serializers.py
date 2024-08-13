"""Serializers for Orders App."""

from rest_framework import serializers

from apps.utilities.mixins import ReadOnlyFieldsMixin
from apps.users.serializers import UserMinimalSerializer
from apps.restaurants.serializers import (
    RestaurantMinimalSerializer,
    FoodMinimalSerializer,
)
from .models import Order, OrderItem, OrderReport, OrderRating
from .services import OrderItemService


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
            "transaction",
            "address_1",
            "address_2",
            "city_id",
            "state_id",
            "country_id",
            "note",
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
            "address_1",
            "address_2",
            "city_id",
            "state_id",
            "country_id",
            "note",
            "restaurant_id",
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

    food_id = FoodMinimalSerializer()

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "food_id",
            "quantity",
            "price",
            # "subtotal",
            "updated_at",
            "created_at",
        ]


class OrderItemWriteSerializer(serializers.ModelSerializer):
    """Serializer for OrderItem model (Create/update)."""

    class Meta:
        model = OrderItem
        fields = [
            "food_id",
            "quantity",
        ]

    def validate_quantity(self, value):
        return OrderItemService.validate_quantity(value)


class OrderReportReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for OrderReport model (List/retrieve)."""

    class Meta:
        model = OrderReport
        fields = [
            "order_id",
            "reason",
            "description",
        ]


class OrderReportWriteSerializer(serializers.ModelSerializer):
    """Serializer for OrderReport model (Create/update)."""

    class Meta:
        model = OrderReport
        fields = [
            "reason",
            "description",
        ]


class OrderRatingWriteSerializer(serializers.ModelSerializer):
    """Serializer for OrderRating model (Create/update)."""

    class Meta:
        model = OrderRating
        fields = [
            "rating",
            "comment",
        ]
