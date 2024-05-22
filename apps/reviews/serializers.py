"""Serializers for Reviews App."""

from rest_framework import serializers

from .models import Review


class ReviewReadSerializer(serializers.ModelSerializer):
    """Serializer for Review model (List/retrieve)."""

    user = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "comment",
            "rating",
            "created_at",
            "updated_at",
        ]
