"""Serializers for Jobs App."""

from rest_framework import serializers

from apps.utilities.mixins import ReadOnlyFieldsMixin
from apps.users.serializers import UserMinimalSerializer
from .models import Position, Worker, Applicant


class PositionReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Position model (List/retrieve)."""

    class Meta:
        model = Position
        fields = [
            "id",
            "position",
            "description",
            "created_at",
            "updated_at",
        ]


class PositionWriteSerializer(serializers.ModelSerializer):
    """Serializer for Position model (Create/update)."""

    class Meta:
        model = Position
        fields = [
            "position",
            "description",
        ]


class PositionMinimalSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Position model (Minimal)."""

    class Meta:
        model = Position
        fields = [
            "id",
            "position",
            "created_at",
            "updated_at",
        ]


class WorkerReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Worker model (List/retrieve)."""

    user_id = UserMinimalSerializer()
    city_id = serializers.StringRelatedField()
    state_id = serializers.StringRelatedField()
    country_id = serializers.StringRelatedField()
    status = serializers.CharField(source="get_status_display")
    contract_type = serializers.CharField(source="get_contract_type_display")

    class Meta:
        model = Worker
        fields = [
            "id",
            "user_id",
            "phone_number",
            "address",
            "city_id",
            "state_id",
            "country_id",
            "position_id",
            "hired_date",
            "termination_date",
            "hourly_rate",
            "status",
            "contract_file",
            "is_active",
            "is_full_time",
            "created_at",
            "updated_at",
        ]


class WorkerWriteSerializer(serializers.ModelSerializer):
    """Serializer for Worker model (Create/update)."""

    class Meta:
        model = Worker
        fields = [
            "user_id",
            "phone_number",
            "address",
            "city_id",
            "state_id",
            "country_id",
            "position_id",
            "hired_date",
            "termination_date",
            "hourly_rate",
            "status",
            "contract_type",
            "contract_file",
            "is_active",
            "is_full_time",
        ]


class WorkerMinimalSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Worker model (Minimal)."""

    user_id = serializers.StringRelatedField()
    position_id = serializers.StringRelatedField()
    status = serializers.CharField(source="get_status_display")
    contract_type = serializers.CharField(source="get_contract_type_display")

    class Meta:
        model = Worker
        fields = [
            "id",
            "user_id",
            "position_id",
            "status",
            "contract_type",
            "is_active",
        ]


class ApplicantReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Applicant model (List/retrieve)."""

    user_id = UserMinimalSerializer()
    position_id = PositionMinimalSerializer()
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Applicant
        fields = [
            "id",
            "user_id",
            "phone_number",
            "email",
            "position_id",
            "cv",
            "message",
            "submitted_at",
            "status",
            "created_at",
            "updated_at",
        ]


class ApplicantWriteSerializer(serializers.ModelSerializer):
    """Serializer for Applicant model (Create/update)."""

    class Meta:
        model = Applicant
        fields = [
            "phone_number",
            "email",
            "position_id",
            "cv",
            "message",
        ]


class ApplicantMinimalSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Applicant model (Minimal)."""

    user_id = serializers.StringRelatedField()
    position_id = serializers.StringRelatedField()
    status = serializers.CharField(source="get_status_display")

    class Meta:
        model = Applicant
        fields = [
            "id",
            "user_id",
            "position_id",
            "status",
        ]
