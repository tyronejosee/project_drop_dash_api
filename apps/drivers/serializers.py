"""Serializers for Drivers App."""

from rest_framework import serializers

from .models import Driver
from .choices import Status


class DriverReadSerializer(serializers.ModelSerializer):
    """Serializer for Driver model (List/retrieve)"""
    user = serializers.UUIDField(read_only=True)
    comune = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    status = serializers.ChoiceField(choices=Status.choices)

    class Meta:
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
    """Serializer for Driver model (Create/update)."""

    class Meta:
        model = Driver
        fields = [
            "address",
            "phone",
            "email",
            "birth_date",
            "comune",
            "region"
        ]
