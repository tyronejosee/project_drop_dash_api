"""Serializers for Users App."""

from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class UserSerializer(UserCreateSerializer):
    """Serializer for User model."""

    class Meta(UserCreateSerializer.Meta):
        """Meta definition for UserSerializer."""
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "role",
            "is_active",
            "is_staff",
            "date_joined"
        ]
