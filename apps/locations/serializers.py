"""Serializers for Locations App."""

from rest_framework.serializers import ModelSerializer

from .models import Country, State, City


class CountryReadSerializer(ModelSerializer):
    """Serializer for Country model (List/retrieve)."""

    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]


class StateReadSerializer(ModelSerializer):
    """Serializer for State model (List/retrieve)."""

    class Meta:
        model = State
        fields = [
            "id",
            "name",
            "created_at",
            "updated_at",
        ]


class StateMinimalSerializer(ModelSerializer):
    """Serializer for State model (Minimal)."""

    class Meta:
        model = State
        fields = [
            "id",
            "name",
        ]


class CityReadSerializer(ModelSerializer):
    """Serializer for City model (List/retrieve)."""

    state_id = StateReadSerializer()

    class Meta:
        model = City
        fields = [
            "id",
            "name",
            "state_id",
            "created_at",
            "updated_at",
        ]


class CityMinimalSerializer(ModelSerializer):
    """Serializer for City model (Minimal)."""

    class Meta:
        model = City
        fields = [
            "id",
            "name",
        ]
