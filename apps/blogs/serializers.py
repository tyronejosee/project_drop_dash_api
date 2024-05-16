"""Serializers for Blogs App."""

from rest_framework.serializers import ModelSerializer

from .models import Post, Tag


class TagReadSerializer(ModelSerializer):
    """Serializer for Category model (List/retrieve)."""

    class Meta:
        model = Tag
        fields = ["id", "name", "slug"]
        read_only_fields = ["id", "slug"]


class TagWriteSerializer(ModelSerializer):
    """Serializer for Category model (Create/update)."""

    class Meta:
        model = Tag
        fields = ["name"]


class PostReadSerializer(ModelSerializer):
    """Serializer for Post model (List/retrieve)."""

    tags = TagReadSerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "tags",
            "author",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["slug", "created_at", "updated_at"]


class PostWriteSerializer(ModelSerializer):
    """Serializer for Post model (Create/update)."""

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]
