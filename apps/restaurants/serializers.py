"""Serializers for Restaurants App."""

from rest_framework import serializers

from .models import Restaurant, Category, Food


class RestaurantReadSerializer(serializers.ModelSerializer):
    """Serializer for Restaurant model (List/retrieve)."""

    city = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    country = serializers.StringRelatedField()

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
            "city",
            "state",
            "country",
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
            "city",
            "state",
            "country",
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
        read_only_fields = fields

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
            "updated_at",
        ]


class CategoryWriteSerializer(serializers.ModelSerializer):
    """Serializer for Category model (Create/update)."""

    class Meta:
        model = Category
        fields = [
            "name",
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
            "category",
            "is_vegetarian",
            "is_gluten_free",
            "is_spicy",
            "is_featured",
        ]
        extra_kwargs = {"category": {"required": True}}


class FoodMiniSerializer(serializers.ModelSerializer):
    """Serializer for Food model (Mini)."""

    class Meta:
        model = Food
        fields = [
            "id",
            "name",
        ]
