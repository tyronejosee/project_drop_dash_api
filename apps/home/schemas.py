"""Schemas for Home App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    CompanyReadSerializer,
    PageReadSerializer,
    PageWriteSerializer,
    PageMinimalSerializer,
    KeywordReadSerializer,
    KeywordWriteSerializer,
)


company_schemas = {
    "get": extend_schema(
        summary="Get Company Data",
        description="Get detailed information about company.",
        responses={
            200: OpenApiResponse(CompanyReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["company"],
    ),
}


page_schemas = {
    "list": extend_schema(
        summary="Get Several Pages",
        description="Get a list of all available pages.",
        responses={
            200: OpenApiResponse(PageMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["pages"],
    ),
    "create": extend_schema(
        summary="Create a Page",
        description="Create a new page, only for `IsMarketing` or `IsAdministrator` users.",
        request=PageWriteSerializer,
        responses={
            201: OpenApiResponse(PageWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["pages"],
    ),
    "retrieve": extend_schema(
        summary="Get a Page",
        description="Get detailed information about a specific page.",
        responses={
            200: OpenApiResponse(PageReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["pages"],
    ),
    "update": extend_schema(
        summary="Update a Page",
        description="Update all fields of a specific page, only for `IsMarketing` or `IsAdministrator` users.",
        request=PageWriteSerializer,
        responses={
            200: OpenApiResponse(PageWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["pages"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Page",
        description="Update some fields of a specific page, only for `IsMarketing` or `IsAdministrator` users.",
        request=PageWriteSerializer,
        responses={
            200: OpenApiResponse(PageWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["pages"],
    ),
    "destroy": extend_schema(
        summary="Remove a Page",
        description="Remove a specific page, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["pages"],
    ),
}


keyword_schemas = {
    "list": extend_schema(
        summary="Get Several Keywords",
        description="Get a list of all available keywords.",
        responses={
            200: OpenApiResponse(KeywordReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["keywords"],
    ),
    "create": extend_schema(
        summary="Create a Keyword",
        description="Create a new keyword, only for `IsMarketing` or `IsAdministrator` users.",
        request=KeywordWriteSerializer,
        responses={
            201: OpenApiResponse(KeywordWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["keywords"],
    ),
    "retrieve": extend_schema(
        summary="Get a Keyword",
        description="Get detailed information about a specific keyword.",
        responses={
            200: OpenApiResponse(KeywordReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["keywords"],
    ),
    "update": extend_schema(
        summary="Update a Keyword",
        description="Update all fields of a specific keyword, only for `IsMarketing` or `IsAdministrator` users.",
        request=KeywordWriteSerializer,
        responses={
            200: OpenApiResponse(KeywordWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["keywords"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Keyword",
        description="Update some fields of a specific keyword, only for `IsMarketing` or `IsAdministrator` users.",
        request=KeywordWriteSerializer,
        responses={
            200: OpenApiResponse(KeywordWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["keywords"],
    ),
    "destroy": extend_schema(
        summary="Remove a Keyword",
        description="Remove a specific keyword, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["keywords"],
    ),
}
