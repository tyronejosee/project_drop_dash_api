"""Serializers for Foods App."""

from rest_framework import serializers

from apps.restaurants.serializers import RestaurantListSerializer
from .models import Food


class FoodSerializer(serializers.ModelSerializer):
    """Serializer for Food model."""
    restaurant = RestaurantListSerializer(read_only=True)
    category = serializers.StringRelatedField()

    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "price",
            "sale_price",
            "image",
            "restaurant",
            "category",
            "is_vegetarian",
            "is_gluten_free",
            "is_spicy",
            "is_featured",
            "created_at",
            "updated_at"
        ]


class FoodMiniSerializer(serializers.ModelSerializer):
    """Serializer for Food model (Mini)."""

    class Meta:
        model = Food
        fields = [
            "id",
            "name"
        ]
