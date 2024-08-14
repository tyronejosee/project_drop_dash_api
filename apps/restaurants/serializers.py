"""Serializers for Restaurants App."""

from rest_framework import serializers

from apps.utilities.mixins import ReadOnlyFieldsMixin
from .models import Restaurant, Category, Food


class RestaurantReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Restaurant model (List/retrieve)."""

    city_id = serializers.StringRelatedField()
    state_id = serializers.StringRelatedField()
    country_id = serializers.StringRelatedField()

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
            "city_id",
            "state_id",
            "country_id",
            "opening_time",
            "closing_time",
            "phone",
            "website",
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
            "city_id",
            "state_id",
            "country_id",
            "phone",
            "opening_time",
            "closing_time",
            "website",
            "banking_certificate",
            "e_rut",
            "legal_rep_email",
            "legal_rep_identity_document",
            "legal_rep_power_of_attorney",
        ]


class RestaurantMinimalSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Restaurant model (Minimal)."""

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

    restaurant_id = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "restaurant_id",
            "created_at",
            "updated_at",
        ]


class CategoryWriteSerializer(serializers.ModelSerializer):
    """Serializer for Category model (Create/update)."""

    class Meta:
        model = Category
        fields = [
            "name",
        ]


class CategoryMinimalSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Category model (Minimal)."""

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class FoodReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Food model (List/retrieve)."""

    category_id = serializers.StringRelatedField()

    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "description",
            "price",
            "sale_price",
            "image",
            "category_id",
            "is_featured",
            "created_at",
            "updated_at",
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
            "category_id",
            "is_featured",
        ]
        extra_kwargs = {"category_id": {"required": True}}


class FoodMinimalSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Food model (Minimal)."""

    class Meta:
        model = Food
        fields = [
            "id",
            "name",
            "price",
            "sale_price",
            "image",
            "category_id",
            "created_at",
            "updated_at",
        ]
