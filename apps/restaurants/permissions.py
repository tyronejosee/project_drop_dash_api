"""Permissions for Restaurants App."""

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsBusinessOwnerOrReadOnly(BasePermission):
    """Permission to only allow business owners to edit the restaurant."""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user.role == "business"
