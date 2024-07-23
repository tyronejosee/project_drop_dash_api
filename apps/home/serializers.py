"""Serializers for Home App."""

from rest_framework.serializers import ModelSerializer

from apps.utilities.mixins import ReadOnlyFieldsMixin
from .models import Keyword


class KeywordMinimalSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for Keyword model (Minimal)."""

    class Meta:
        model = Keyword
        fields = ["word", "slug"]
