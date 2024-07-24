"""Serializers for Locations App."""

from rest_framework.serializers import ModelSerializer

from apps.utilities.mixins import ReadOnlyFieldsMixin
from .models import Country, State, City


class CountryReadSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for Country model (List/retrieve)."""

    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]


class CountryWriteSerializer(ModelSerializer):
    """Serializer for Country model (Create/update)."""

    class Meta:
        model = Country
        fields = [
            "name",
        ]


class CountryMinimalSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for Country model (Minimal)."""

    class Meta:
        model = Country
        fields = [
            "id",
            "name",
        ]


class StateReadSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for State model (List/retrieve)."""

    country_id = CountryMinimalSerializer()

    class Meta:
        model = State
        fields = [
            "id",
            "name",
            "country_id",
            "created_at",
            "updated_at",
        ]


class StateWriteSerializer(ModelSerializer):
    """Serializer for State model (Create/update)."""

    class Meta:
        model = State
        fields = [
            "name",
            "country_id",
        ]


class StateMinimalSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for State model (Minimal)."""

    class Meta:
        model = State
        fields = [
            "id",
            "name",
        ]


class CityReadSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for City model (List/retrieve)."""

    state_id = StateMinimalSerializer()

    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "state_id",
            "created_at",
            "updated_at",
        ]


class CityWriteSerializer(ModelSerializer):
    """Serializer for City model (Create/update)."""

    class Meta:
        model = City
        fields = [
            "name",
            "state_id",
        ]


class CityMinimalSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for City model (Minimal)."""

    class Meta:
        model = City
        fields = [
            "id",
            "name",
        ]
