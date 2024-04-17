"""Serializers for Categories App."""

from rest_framework import serializers

from apps.restaurants.serializers import RestaurantSerializer
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    restaurant = RestaurantSerializer(read_only=True)

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
