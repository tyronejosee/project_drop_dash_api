"""Serializers for Foods App."""

from rest_framework.serializers import ModelSerializer

from .models import Food


class FoodSerializer(ModelSerializer):
    """Serializer for Food model."""

    class Meta:
        """Meta definition for FoodSerializer."""
        model = Food
        fields = [
            "id",
            "name",
            "description",
            "normal_price",
            "sale_price",
            "preparation_time",
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
