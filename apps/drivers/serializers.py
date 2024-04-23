"""Serializers for Drivers App."""

from rest_framework import serializers

from apps.users.serializers import UserSerializer
from .models import Driver


class DriverSerializer(serializers.ModelSerializer):
    """Serializer for Driver model."""
    user = UserSerializer()
    comune = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    status = serializers.CharField(source="get_status_display", read_only=True)

    class Meta:
        """Meta definition for DriverSerializer."""
        model = Driver
        fields = [
            "id",
            "user",
            "address",
            "phone",
            "email",
            "birth_date",
            "comune",
            "region",
            "status"
        ]