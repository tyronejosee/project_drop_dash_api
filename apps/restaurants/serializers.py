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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = data.get("image", "") or ""
        data["banner"] = data.get("banner", "") or ""
        return data


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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = data.get("image", "") or ""
        return data


class CategoryReadSerializer(serializers.ModelSerializer):
    """Serializer for Category model (List/retrieve)."""
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


class CategoryWriteSerializer(serializers.ModelSerializer):
    """Serializer for Category model (Create/update)."""

    class Meta:
        model = Category
        fields = [
            "name"
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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = data.get("image", "") or ""
        return data


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
