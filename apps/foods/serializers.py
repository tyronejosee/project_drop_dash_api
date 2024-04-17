"""Serializers for Foods App."""

from rest_framework.serializers import ModelSerializer

from apps.restaurants.serializers import RestaurantListSerializer
from apps.categories.serializers import CategorySerializer
from .models import Food


class FoodSerializer(ModelSerializer):
    """Serializer for Food model."""
    restaurant = RestaurantListSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        """Meta definition for FoodSerializer."""
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
