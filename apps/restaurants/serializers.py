"""Serializers for Restaurants App."""

from rest_framework import serializers

from .models import Restaurant, Category, Food


class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer for Restaurant model."""

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "slug",
            "image",
            "banner",
            "description",
            "specialty",
            "address",
            "opening_time",
            "closing_time",
            "phone",
            "email",
            "facebook",
            "instagram",
            "tiktok",
            "website",
            "is_open",
            "created_at",
            "updated_at"
        ]


class RestaurantListSerializer(serializers.ModelSerializer):
    """Serializer for Restaurant model (List only)."""

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "slug",
            "image",
        ]


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    restaurant = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "restaurant",
            "created_at",
            "updated_at"
        ]


class CategoryListSerializer(serializers.ModelSerializer):
    """Serializer for Category model (List only)."""

    class Meta:
        model = Category
        fields = [
            "id",
            "name"
        ]


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
