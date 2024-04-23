"""Serializers for Categories App."""

from rest_framework import serializers

from .models import Category


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
