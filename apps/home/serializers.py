"""Serializers for Home App."""

from rest_framework.serializers import ModelSerializer

from apps.utilities.mixins import ReadOnlyFieldsMixin
from .models import Page, Keyword


class PageReadSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for Page model (List/retrieve)."""

    class Meta:
        model = Page
        fields = [
            "id",
            "name",
            "slug",
            "content",
            "created_at",
            "updated_at",
        ]


class PageWriteSerializer(ModelSerializer):
    """Serializer for Page model (Create/update)."""

    class Meta:
        model = Page
        fields = [
            "name",
            "content",
        ]


class PageMinimalSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for Page model (Minimal)."""

    class Meta:
        model = Page
        fields = [
            "id",
            "name",
        ]


class KeywordReadSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for Keyword model (List/retrieve)."""

    class Meta:
        model = Keyword
        fields = [
            "id",
            "word",
            "slug",
            "created_at",
            "updated_at",
        ]


class KeywordWriteSerializer(ModelSerializer):
    """Serializer for Keyword model (Create/update)."""

    class Meta:
        model = Keyword
        fields = [
            "word",
        ]
