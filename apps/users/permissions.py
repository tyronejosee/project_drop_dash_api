"""Permissions for Utilities App."""

from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    """
    Allows access only to users with the role "client".
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = (
            request.user.is_active and request.user.role == "client"
        )
        return bool(is_user_authenticated and is_user_valid)


class IsDriver(BasePermission):
    """
    Allows access only to users with the role "driver".
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = (
            request.user.is_active and request.user.role == "driver"
        )
        return bool(is_user_authenticated and is_user_valid)


class IsBusiness(BasePermission):
    """
    Allows access only to users with the role "business".
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = (
            request.user.is_active and request.user.role == "business"
        )
        return bool(is_user_authenticated and is_user_valid)


class IsSupport(BasePermission):
    """
    Allows access only to users with the role "support".
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = (
            request.user.is_active and request.user.role == "support"
        )
        return bool(is_user_authenticated and is_user_valid)


class IsAdministrator(BasePermission):
    """
    Allows access only to Administrator users.
    """

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = (
            request.user.is_active and request.user.role == "administrator"
        )
        return bool(is_user_authenticated and is_user_valid)
