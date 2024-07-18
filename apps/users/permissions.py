"""Permissions for Utilities App."""

from rest_framework.permissions import BasePermission

from .choices import RoleChoices


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


class IsAdvertiser(BaseRolePermission):
    """
    Allows access only to users with the role "advertiser".
    """

    required_roles = [
        RoleChoices.ADVERTISER,
        RoleChoices.ADMINISTRATOR,
    ]


class IsClient(BaseRolePermission):
    """
    Allows access only to users with the role "client".
    """

    required_roles = [
        RoleChoices.CLIENT,
        RoleChoices.ADMINISTRATOR,
    ]


class IsDriver(BaseRolePermission):
    """
    Allows access only to users with the role "driver".
    """

    required_roles = [
        RoleChoices.DRIVER,
        RoleChoices.ADMINISTRATOR,
    ]


class IsDispatcher(BaseRolePermission):
    """
    Allows access only to users with the role "dispatcher".
    """

    required_roles = [
        RoleChoices.DISPATCHER,
        RoleChoices.ADMINISTRATOR,
    ]


class IsPartner(BaseRolePermission):
    """
    Allows access only to users with the role "business".
    """

    required_roles = [
        RoleChoices.PARTNER,
        RoleChoices.ADMINISTRATOR,
    ]


class IsSupport(BaseRolePermission):
    """
    Allows access only to users with the role "support".
    """

    required_roles = [
        RoleChoices.SUPPORT,
        RoleChoices.ADMINISTRATOR,
    ]


class IsMarketing(BaseRolePermission):
    """
    Allows access only to users with the role "Marketing".
    """

    required_roles = [
        RoleChoices.MARKETING,
        RoleChoices.ADMINISTRATOR,
    ]


class IsOperations(BaseRolePermission):
    """
    Allows access only to users with the role "operations".
    """

    required_roles = [
        RoleChoices.OPERATIONS,
        RoleChoices.ADMINISTRATOR,
    ]


class IsFinance(BaseRolePermission):
    """
    Allows access only to users with the role "finance".
    """

    required_roles = [
        RoleChoices.FINANCE,
        RoleChoices.ADMINISTRATOR,
    ]


class IsHumanResources(BaseRolePermission):
    """
    Allows access only to users with the role "human_resources".
    """

    required_roles = [
        RoleChoices.HUMAN_RESOURCES,
        RoleChoices.ADMINISTRATOR,
    ]


class IsAdministrator(BaseRolePermission):
    """
    Allows access only to Administrator users.
    """

    required_roles = [RoleChoices.ADMINISTRATOR]
