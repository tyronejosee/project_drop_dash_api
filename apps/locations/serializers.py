"""Serializers for Locations App."""

from rest_framework.serializers import ModelSerializer

from .models import Region, Comune


class RegionSerializer(ModelSerializer):
    """Serializer for Region model."""

    class Meta:
        """Meta definition for RegionSerializer."""
        model = Region
        fields = [
            "id",
            "name",
            "number",
            "is_metropolitan",
            "created_at",
            "updated_at"
        ]


class RegionListSerializer(ModelSerializer):
    """Serializer for Region model (List only)."""

    class Meta:
        """Meta definition for RegionListSerializer."""
        model = Region
        fields = [
            "id",
            "name",
        ]


class ComuneSerializer(ModelSerializer):
    """Serializer for Comune model."""
    region = RegionSerializer()

    class Meta:
        """Meta definition for ComuneSerializer."""
        model = Comune
        fields = [
            "id",
            "name",
            "region",
            "created_at",
            "updated_at"
        ]


class ComuneListSerializer(ModelSerializer):
    """Serializer for Comune model (List only)."""

    class Meta:
        """Meta definition for ComuneListSerializer."""
        model = Comune
        fields = [
            "id",
            "name"
        ]
