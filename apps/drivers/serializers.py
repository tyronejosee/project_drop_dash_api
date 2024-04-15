"""Serializers for Drivers App."""

from rest_framework.serializers import ModelSerializer

from apps.locations.serializers import ComuneSerializer, RegionSerializer
from .models import Driver


class DriverSerializer(ModelSerializer):
    """Serializer for Driver model."""
    comune = ComuneSerializer(read_only=True)
    region = RegionSerializer(read_only=True)

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
            "status",
            "created_at",
            "updated_at"
        ]
