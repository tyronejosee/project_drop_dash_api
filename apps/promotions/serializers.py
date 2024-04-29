"""Serializers for Promotions App."""

from rest_framework.serializers import ModelSerializer

from .models import Promotion


class PromotionSerializer(ModelSerializer):
    """Serializer for Promotion model."""

    class Meta:
        """Meta definition for PromotionSerializer."""
        model = Promotion
        fields = [
            "id",
            "creator",
            "name",
            "conditions",
            "start_date",
            "end_date",
            "is_active",
            "image"
        ]
