"""Serializers for Promotions App."""

from datetime import datetime, timedelta
from rest_framework.serializers import ModelSerializer, ValidationError

from apps.users.serializers import UserMinimalSerializer
from .models import Promotion


class PromotionReadSerializer(ModelSerializer):
    """Serializer for Promotion model (List/retrieve)."""
    creator = UserMinimalSerializer()

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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data["image"] is None:
            data["image"] = ""
        return data


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

    def validate_start_date(self, value):
        """Validate that start_date is not earlier than the current month."""
        if value.month < datetime.now().month:
            raise ValidationError(
                "Start date cannot be earlier than the current month."
            )
        return value

    def validate_end_date(self, value):
        """Validate that end_date is not more than 90 days."""
        if isinstance(value, datetime):
            value = value.date()

        if value > datetime.now().date() + timedelta(days=90):
            raise ValidationError(
                "End date cannot be more than 90 days from the current date."
            )
        return value
