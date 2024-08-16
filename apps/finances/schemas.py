"""Schemas for Finances App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import RevenueReadSerializer, RevenueWriteSerializer


revenue_schemas = {
    "list": extend_schema(
        summary="Get Several Revenues",
        description="Get a list of all available revenues, only for `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(RevenueReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["revenues"],
    ),
    "create": extend_schema(
        summary="Create a Revenue",
        description="Create a new revenue, only for `IsAdministrator` users.",
        request=RevenueWriteSerializer,
        responses={
            201: OpenApiResponse(RevenueWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["revenues"],
    ),
    "retrieve": extend_schema(
        summary="Get a Revenue",
        description="Get detailed information about a specific revenue, only for `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(RevenueReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["revenues"],
    ),
    "update": extend_schema(
        summary="Update a Revenue",
        description="Update all fields of a specific revenue, only for `IsAdministrator` users.",
        request=RevenueWriteSerializer,
        responses={
            200: OpenApiResponse(RevenueWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["revenues"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Revenue",
        description="Update some fields of a specific revenue, only for `IsAdministrator` users.",
        request=RevenueWriteSerializer,
        responses={
            200: OpenApiResponse(RevenueWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["revenues"],
    ),
    "destroy": extend_schema(
        summary="Remove a Revenue",
        description="Remove a specific revenue, only for `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["revenues"],
    ),
}
