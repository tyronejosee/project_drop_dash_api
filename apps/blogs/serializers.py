"""Serializers for Blogs App."""

from rest_framework.serializers import ModelSerializer

from .models import Post, Tag


class TagSerializer(ModelSerializer):
    """Serializer for Category model."""

    class Meta:
        """Meta definition for TagSerializer."""
        model = Tag
        fields = [
            "id",
            "name",
            "slug"
        ]
        read_only_fields = ["slug",]


class PostSerializer(ModelSerializer):
    """Serializer for Post model."""
    tags = TagSerializer(many=True)

    class Meta:
        """Meta definition for PostSerializer."""
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "tags"
            "author",
            "created_at",
            "updated_at"
        ]
        read_only_fields = ["slug", "created_at", "updated_at"]
