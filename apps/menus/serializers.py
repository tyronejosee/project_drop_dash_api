"""Serializers for Menus App."""

from rest_framework.serializers import ModelSerializer

from apps.users.serializers import UserSerializer
from apps.restaurants.serializers import RestaurantSerializer
from apps.foods.serializers import FoodSerializer
from .models import Menu, MenuItem


class MenuSerializer(ModelSerializer):
    """Serializer for Menu model."""
    user = UserSerializer(read_only=True)
    restaurant = RestaurantSerializer(read_only=True)

    class Meta:
        """Meta definition for MenuSerializer."""
        model = Menu
        fields = [
            "id",
            "user",
            "restaurant",
            "created_at",
            "updated_at"
        ]


class MenuItemSerializer(ModelSerializer):
    """Serializer for MenuItem model."""
    menu = MenuSerializer(read_only=True)
    food = FoodSerializer(read_only=True)

    class Meta:
        """Meta definition for MenuItemSerializer."""
        model = MenuItem
        fields = [
            "id",
            "menu",
            "food"
        ]
