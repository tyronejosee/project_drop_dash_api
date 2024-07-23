"""Serializers for Blogs App."""

from rest_framework.serializers import ModelSerializer, CharField, StringRelatedField

from apps.utilities.mixins import ReadOnlyFieldsMixin
from .models import Post, Tag, PostReport


class TagReadSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for Category model (List/retrieve)."""

    class Meta:
        model = Tag
        fields = [
            "id",
            "name",
            "slug",
        ]


class TagWriteSerializer(ModelSerializer):
    """Serializer for Category model (Create/update)."""

    class Meta:
        model = Tag
        fields = ["name"]


class PostReadSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for Post model (List/retrieve)."""

    tags = TagReadSerializer(many=True)
    author_id = StringRelatedField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "slug",
            "content",
            "tags",
            "author_id",
            "created_at",
            "updated_at",
        ]


class PostWriteSerializer(ModelSerializer):
    """Serializer for Post model (Create/update)."""

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "tags",
        ]


class PostReportReadSerializer(ReadOnlyFieldsMixin, ModelSerializer):
    """Serializer for PostReport model (List)."""

    priority = CharField(source="get_priority_display")
    status = CharField(source="get_status_display")

    class Meta:
        model = PostReport
        fields = [
            "id",
            "user_id",
            "post_id",
            "reason",
            "priority",
            "status",
            "created_at",
            "updated_at",
        ]


class PostReportWriteSerializer(ModelSerializer):
    """Serializer for PostReport model (Create)."""

    class Meta:
        model = PostReport
        fields = [
            "reason",
        ]
