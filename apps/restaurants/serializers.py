"""Serializers for Restaurants App."""

from rest_framework import serializers

from .models import Restaurant, Category, Food


class RestaurantReadSerializer(serializers.ModelSerializer):
    """Serializer for Restaurant model (List/retrieve)."""

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
            "comune",
            "region",
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


class RestaurantWriteSerializer(serializers.ModelSerializer):
    """Serializer for Restaurant model."""

    class Meta:
        model = Restaurant
        fields = [
            "name",
            "image",
            "banner",
            "description",
            "specialty",
            "address",
            "comune",
            "region",
            "opening_time",
            "closing_time",
            "phone",
            "email",
            "facebook",
            "instagram",
            "tiktok",
            "website"
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


class FoodReadSerializer(serializers.ModelSerializer):
    """Serializer for Food model (List/retrieve)."""
    category = serializers.StringRelatedField()

    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "price",
            "sale_price",
            "image",
            "category",
            "is_vegetarian",
            "is_gluten_free",
            "is_spicy",
            "is_featured",
            "created_at",
            "updated_at"
        ]


class FoodWriteSerializer(serializers.ModelSerializer):
    """Serializer for Food model (Create/update)."""

    class Meta:
        model = Food
        fields = [
            "name",
            "price",
            "image",
            "category",
            "is_vegetarian",
            "is_gluten_free",
            "is_spicy",
            "is_featured"
        ]
        extra_kwargs = {
            "category": {"required": True}
        }


class FoodMiniSerializer(serializers.ModelSerializer):
    """Serializer for Food model (Mini)."""

    class Meta:
        model = Food
        fields = [
            "id",
            "name"
        ]
