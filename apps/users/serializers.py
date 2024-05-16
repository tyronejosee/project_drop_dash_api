"""Serializers for Users App."""

from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class UserReadSerializer(UserCreateSerializer):
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
            "identity_number",
            "phone",
            "points",
            "role",
            "is_active",
            "is_staff",
            "created_at",
            "updated_at",
        ]


class UserMinimalSerializer(UserCreateSerializer):
    """Serializer for User model (Minimal version)."""

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "email",
            "role",
            "is_staff",
        ]
