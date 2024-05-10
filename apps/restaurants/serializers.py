"""Serializers for Restaurants App."""

from rest_framework import serializers

from .models import Restaurant, Category


class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer for Restaurant model."""

    class Meta:
        """Meta definition for RestaurantSerializer."""
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
        """Meta definition for RestaurantSerializer."""
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
        """Meta definition for CategorySerializer."""
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
        """Meta definition for CategoryListSerializer."""
        model = Category
        fields = [
            "id",
            "name"
        ]
