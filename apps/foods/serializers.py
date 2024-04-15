"""Serializers for Foods App."""

from rest_framework.serializers import ModelSerializer

from apps.restaurants.serializers import RestaurantSerializer
from apps.categories.serializers import CategorySerializer
from .models import Food


class FoodSerializer(ModelSerializer):
    """Serializer for Food model."""
    restaurant = RestaurantSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

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
