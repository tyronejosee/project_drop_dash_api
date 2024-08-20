"""Schemas for Users App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    UserReadSerializer,
    UserWriteSerializer,
    UserMinimalSerializer,
)


user_schemas = {
    "list": extend_schema(
        summary="Get Several Users",
        description="Get a list of all available users.",
        responses={
            200: OpenApiResponse(UserMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["users"],
    ),
    "create": extend_schema(
        summary="Create a User",
        description="Create a new user, only for `IsExample` or `IsAdministrator` users.",
        request=UserWriteSerializer,
        responses={
            201: OpenApiResponse(UserWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["users"],
    ),
    "retrieve": extend_schema(
        summary="Get a User",
        description="Get detailed information about a specific user.",
        responses={
            200: OpenApiResponse(UserReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["users"],
    ),
    "update": extend_schema(
        summary="Update a User",
        description="Update all fields of a specific user, only for `IsExample` or `IsAdministrator` users.",
        request=UserWriteSerializer,
        responses={
            200: OpenApiResponse(UserWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["users"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a User",
        description="Update some fields of a specific user, only for `IsExample` or `IsAdministrator` users.",
        request=UserWriteSerializer,
        responses={
            200: OpenApiResponse(UserWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["users"],
    ),
    "destroy": extend_schema(
        summary="Remove a User",
        description="Remove a specific user, only for `IsExample` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["users"],
    ),
    "me": extend_schema(
        summary="Get Me",
        description="Pending.",
        tags=["users"],
    ),
    "activation": extend_schema(
        summary="Activation",
        description="Pending.",
        tags=["users"],
    ),
    "resend_activation": extend_schema(
        summary="Resend Activation",
        description="Pending.",
        tags=["users"],
    ),
    "set_password": extend_schema(
        summary="Resend Activation",
        description="Pending.",
        tags=["users"],
    ),
    "reset_password": extend_schema(
        summary="Reset Password",
        description="Pending.",
        tags=["users"],
    ),
    "reset_password_confirm": extend_schema(
        summary="Reset Password Confirm",
        description="Pending.",
        tags=["users"],
    ),
    "set_username": extend_schema(
        summary="Set Username",
        description="Pending.",
        tags=["users"],
    ),
    "reset_username": extend_schema(
        summary="Set Username",
        description="Pending.",
        tags=["users"],
    ),
    "reset_username_confirm": extend_schema(
        summary="Reset Username Confirm",
        description="Pending.",
        tags=["users"],
    ),
}


token_obtain_pair_schemas = {
    "post": extend_schema(
        summary="Token Obtain Pair",
        description="Pending.",
        tags=["tokens"],
    ),
}


token_refresh_schemas = {
    "post": extend_schema(
        summary="Token Refresh",
        description="Pending.",
        tags=["tokens"],
    ),
}


token_verify_schemas = {
    "post": extend_schema(
        summary="Token Verify",
        description="Pending.",
        tags=["tokens"],
    ),
}
