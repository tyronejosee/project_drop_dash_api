"""Serializers for Categories App."""

from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""

    class Meta:
        """Meta definition for CategorySerializer."""
        model = Category
        fields = [
            "id",
            "name",
            "description",
            "slug",
            "created_at",
            "updated_at"
        ]
