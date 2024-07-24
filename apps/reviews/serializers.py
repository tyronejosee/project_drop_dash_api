"""Serializers for Reviews App."""

from rest_framework import serializers

from apps.utilities.mixins import ReadOnlyFieldsMixin
from .models import Review


class ReviewReadSerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for Review model (List/retrieve)."""

    user_id = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = [
            "id",
            "user_id",
            "comment",
            "rating",
            "created_at",
            "updated_at",
        ]


class ReviewWriteSerializer(serializers.ModelSerializer):
    """Serializer for Review model (Create/update)."""

    class Meta:
        model = Review
        fields = [
            "comment",
            "rating",
        ]
