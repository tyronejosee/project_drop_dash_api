"""Serializers for Promotions App."""

from rest_framework.serializers import ModelSerializer

from apps.users.serializers import UserSerializer
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

    def to_representation(self, instance):
        # Overridden method to include serializers for foreign keys
        data = super().to_representation(instance)
        data["creator"] = UserSerializer(instance.creator).data
        return data
