"""Serializers for Users App."""

from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from apps.utilities.mixins import ReadOnlyFieldsMixin

User = get_user_model()


class UserReadSerializer:
    """Serializer for User model."""

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "username",
            "points",
            "role",
        ]


class UserWriteSerializer(UserCreateSerializer):
    """Serializer for User model."""

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "date_birth",
            "points",
            "role",
            "is_active",
            "is_staff",
            "created_at",
            "updated_at",
        ]


class UserMinimalSerializer(ReadOnlyFieldsMixin, UserCreateSerializer):
    """Serializer for User model (Minimal)."""

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "username",
            "role",
        ]


class UserHistorySerializer(ReadOnlyFieldsMixin, serializers.ModelSerializer):
    """Serializer for User history."""

    class Meta:
        model = User.history.model
        fields = [
            "id",
            "username",
            "history_date",
            "history_user",
            "history_type",
        ]
