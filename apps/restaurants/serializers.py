"""Serializers for Restaurants App."""

from rest_framework import serializers

from .models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    """Serializer for Restaurant model."""

    class Meta:
        """Meta definition for RestaurantSerializer."""
        model = Restaurant
        fields = [
            "id",
            "name",
            "slug",
            "image",
            "description",
            "specialty",
            "address",
            "opening_time",
            "closing_time",
            "phone",
            "email",
            "website",
            "is_open",
            "created_at",
            "updated_at"
        ]
