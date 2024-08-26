"""Helpers for Utilities App."""

from rest_framework.response import Response


def generate_response(result):
    """Generate a Response object based on the result dictionary."""
    if result.get("success"):
        return Response(
            {"detail": result.get("message")}, status=result.get("status_code")
        )
    return Response({"error": result.get("message")}, status=result.get("status_code"))


def generate_cache_key(request, prefix="viewset", *args, **kwargs):
    """
    Generate a cache key based on the user's primary key if authenticated,
    or their IP address if not.
    """
    user_pk = request.user.pk if request.user.is_authenticated else None
    user_ip = request.META.get("REMOTE_ADDR", "anonymous")
    if user_pk:
        return str(f"{prefix}_{user_pk}")
    return str(f"{prefix}_{user_ip}")
