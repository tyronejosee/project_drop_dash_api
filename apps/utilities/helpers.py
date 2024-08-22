"""Helpers for Utilities App."""

from rest_framework.response import Response


def generate_response(result):
    """Generate a Response object based on the result dictionary."""
    if result.get("success"):
        return Response(
            {"detail": result.get("message")}, status=result.get("status_code")
        )
    return Response({"error": result.get("message")}, status=result.get("status_code"))
