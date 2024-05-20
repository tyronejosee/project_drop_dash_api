"""Serializers for Drivers App."""

from rest_framework import serializers

from apps.utilities.validators import validate_phone, validate_birth_date
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
            "birth_date",
            "city",
            "state",
            "country",
            "status",
        ]


class DriverWriteSerializer(serializers.ModelSerializer):
    """Serializer for Driver model (Create/update)."""

    phone = serializers.CharField(max_length=12, validators=[validate_phone])
    birth_date = serializers.DateField(validators=[validate_birth_date])
    address = serializers.CharField(max_length=255)

    class Meta:
        model = Driver
        fields = [
            "phone",
            "birth_date",
            "driver_license",
            "identification_document",
            "social_security_certificate",
            "address",
            "city",
            "state",
            "country",
        ]


class ResourceReadSerializer(serializers.ModelSerializer):
    """Serializer for Resource model (List/retrieve)."""

    class Meta:
        model = Resource
        fields = [
            "resource_type",
            "note",
            "status",
        ]


class ResourceWriteSerializer(serializers.ModelSerializer):
    """Serializer for Resource model (Create/update)."""

    class Meta:
        model = Resource
        fields = [
            "resource_type",
            "note",
        ]
        extra_kwargs = {
            "resource_type": {"required": True},
            "note": {"required": True},
        }
