"""Serializers for Promotions App."""

from rest_framework.serializers import ModelSerializer

from apps.users.serializers import UserSerializer
from .models import Promotion


class PromotionReadSerializer(ModelSerializer):
    """Serializer for Promotion model (List/retrieve)."""
    creator = UserSerializer()

    class Meta:
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


class PromotionWriteSerializer(ModelSerializer):
    """Serializer for Promotion model (Create/update)."""

    class Meta:
        model = Promotion
        fields = [
            "name",
            "conditions",
            "start_date",
            "end_date",
            "is_active",
            "image"
        ]
