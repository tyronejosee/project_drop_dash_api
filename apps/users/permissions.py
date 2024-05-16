"""Permissions for Utilities App."""

from rest_framework.permissions import BasePermission

from .choices import Role


class IsClient(BasePermission):
    """
    Allows access only to users with the role "client".
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = request.user.is_active and request.user.role in [
            Role.CLIENT,
            Role.ADMINISTRATOR,
        ]
        return bool(is_user_authenticated and is_user_valid)


class IsDriver(BasePermission):
    """
    Allows access only to users with the role "driver".
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = request.user.is_active and request.user.role in [
            Role.DRIVER,
            Role.ADMINISTRATOR,
        ]
        return bool(is_user_authenticated and is_user_valid)


class IsPartner(BasePermission):
    """
    Allows access only to users with the role "business".
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = request.user.is_active and request.user.role in [
            Role.PARTNER,
            Role.ADMINISTRATOR,
        ]
        return bool(is_user_authenticated and is_user_valid)


class IsSupport(BasePermission):
    """
    Allows access only to users with the role "support".
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = request.user.is_active and request.user.role in [
            Role.SUPPORT,
            Role.ADMINISTRATOR,
        ]
        return bool(is_user_authenticated and is_user_valid)


class IsAdministrator(BasePermission):
    """
    Allows access only to Administrator users.
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = (
            request.user.is_active and request.user.role == Role.ADMINISTRATOR
        )
        return bool(is_user_authenticated and is_user_valid)
