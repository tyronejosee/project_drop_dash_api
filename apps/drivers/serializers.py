"""Serializers for Drivers App."""

from rest_framework import serializers

from apps.utilities.mixins import ReadOnlyFieldsMixin
from apps.utilities.functions import decrypt_field
from apps.utilities.validators import validate_phone, validate_birth_date
from .models import Driver, Resource
from .choices import StatusChoices


class DriverReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Driver model (List/retrieve)"""

    user_id = serializers.UUIDField(read_only=True)
    city_id = serializers.StringRelatedField()
    state_id = serializers.StringRelatedField()
    country_id = serializers.StringRelatedField()
    status = serializers.ChoiceField(choices=StatusChoices.choices)

    class Meta:
        model = Driver
        fields = [
            "id",
            "user_id",
            "address",
            "phone",
            "birth_date",
            "city_id",
            "state_id",
            "country_id",
            "status",
            "updated_at",
            "created_at",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["phone"] = decrypt_field(data["phone"])
        data["address"] = decrypt_field(data["address"])
        return data


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
            "criminal_record_certificate",
            "social_security_certificate",
            "address",
            "city_id",
            "state_id",
            "country_id",
            "vehicle_type",
        ]


class DriverMinimalSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Driver model (Minimal)"""

    user_id = serializers.StringRelatedField()
    city_id = serializers.StringRelatedField()
    state_id = serializers.StringRelatedField()
    country_id = serializers.StringRelatedField()
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Driver
        fields = [
            "id",
            "user_id",
            "city_id",
            "state_id",
            "country_id",
            "status",
        ]


class ResourceReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
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
