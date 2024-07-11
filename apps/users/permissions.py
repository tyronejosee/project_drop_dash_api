"""Permissions for Utilities App."""

from rest_framework.permissions import BasePermission

from .choices import Role


class BaseRolePermission(BasePermission):
    """
    Base permission class that checks if a user has a specific role.
    """

    required_roles = []

    def has_permission(self, request, view):
        is_user_authenticated = request.user and request.user.is_authenticated
        is_user_valid = (
            request.user.is_active and request.user.role in self.required_roles
        )
        return bool(is_user_authenticated and is_user_valid)


class IsClient(BaseRolePermission):
    """
    Allows access only to users with the role "client".
    """

    required_roles = [
        Role.CLIENT,
        Role.ADMINISTRATOR,
    ]


class IsDriver(BaseRolePermission):
    """
    Allows access only to users with the role "driver".
    """

    required_roles = [
        Role.DRIVER,
        Role.ADMINISTRATOR,
    ]


class IsPartner(BaseRolePermission):
    """
    Allows access only to users with the role "business".
    """

    required_roles = [
        Role.PARTNER,
        Role.ADMINISTRATOR,
    ]


class IsMarketing(BaseRolePermission):
    """
    Allows access only to users with the role "Marketing".
    """

    required_roles = [
        Role.MARKETING,
        Role.ADMINISTRATOR,
    ]


class IsSupport(BaseRolePermission):
    """
    Allows access only to users with the role "support".
    """

    required_roles = [
        Role.SUPPORT,
        Role.ADMINISTRATOR,
    ]


class IsAdministrator(BaseRolePermission):
    """
    Allows access only to Administrator users.
    """

    required_roles = [
        Role.ADMINISTRATOR
    ]
