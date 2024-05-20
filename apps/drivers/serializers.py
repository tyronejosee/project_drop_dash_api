"""Serializers for Drivers App."""

from rest_framework import serializers

from .models import Driver, Resource
from .choices import Status


class DriverReadSerializer(serializers.ModelSerializer):
    """Serializer for Driver model (List/retrieve)"""

    user = serializers.UUIDField(read_only=True)
    city = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    country = serializers.StringRelatedField()
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
            "city",
            "state",
            "country",
            "status",
        ]


class DriverWriteSerializer(serializers.ModelSerializer):
    """Serializer for Driver model (Create/update)."""

    class Meta:
        model = Driver
        fields = [
            "phone",
            "email",
            "birth_date",
            "address",
            "city",
            "state",
            "country",
        ]


class ResourceWriteSerializer(serializers.ModelSerializer):
    """Serializer for Resource model (Create/update)."""

    class Meta:
        model = Resource
        fields = [
            "resource_type",
            "note",
        ]
