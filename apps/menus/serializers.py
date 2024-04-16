"""Serializers for Menus App."""

from rest_framework.serializers import ModelSerializer

from apps.restaurants.serializers import RestaurantListSerializer
from apps.foods.serializers import FoodSerializer
from .models import Menu


class MenuSerializer(ModelSerializer):
    """Serializer for Menu model."""
    restaurant = RestaurantListSerializer(read_only=True)
    food = FoodSerializer(read_only=True)

    class Meta:
        """Meta definition for MenuSerializer."""
        model = Menu
        fields = [
            "id",
            "restaurant",
            "food"
            "created_at",
            "updated_at"
        ]
