"""Permissions for Restaurants App."""

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsBusinessOrReadOnly(BasePermission):
    """Permission to only allow business owners to edit the restaurant."""

    def has_permission(self, request, view):
        is_safe_method = request.method in SAFE_METHODS
        is_business = (
            request.user.is_authenticated and request.user.role == "business")
        return is_safe_method or is_business
