"""Serializers for Drivers App."""

from rest_framework import serializers

from .models import Driver
from .choices import Status


class DriverReadSerializer(serializers.ModelSerializer):
    """Serializer for reading Driver instances."""
    user = serializers.UUIDField(read_only=True)
    comune = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    status = serializers.ChoiceField(choices=Status.choices)

    class Meta:
        """Meta definition for DriverReadSerializer."""
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


class DriverWriteSerializer(serializers.ModelSerializer):
    """Serializer for creating/updating Driver instances."""

    class Meta:
        """Meta definition for DriverWriteSerializer."""
        model = Driver
        fields = [
            "address",
            "phone",
            "email",
            "birth_date",
            "comune",
            "region"
        ]
