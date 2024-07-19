"""Serializers for Reviews App."""

from rest_framework import serializers

from .models import Review


class ReviewReadSerializer(serializers.ModelSerializer):
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
