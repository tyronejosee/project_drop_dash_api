"""Schemas for Blogs App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    PostReadSerializer,
    PostWriteSerializer,
    TagReadSerializer,
    TagWriteSerializer,
    PostReportReadSerializer,
    PostReportWriteSerializer,
)


post_schemas = {
    "list": extend_schema(
        summary="Get Several Posts",
        description="Get a list of all available posts.",
        responses={
            200: OpenApiResponse(PostReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["blogs"],
    ),
    "create": extend_schema(
        summary="Create a Post",
        description="Create a new post, only for `IsMarketing` or `IsAdministrator` users.",
        request=PostWriteSerializer,
        responses={
            201: OpenApiResponse(PostWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["blogs"],
    ),
    "retrieve": extend_schema(
        summary="Get a Post",
        description="Get detailed information about a specific post.",
        responses={
            200: OpenApiResponse(PostReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["blogs"],
    ),
    "update": extend_schema(
        summary="Update a Post",
        description="Update all fields of a specific post, only for `IsMarketing` or `IsAdministrator` users.",
        request=PostWriteSerializer,
        responses={
            200: OpenApiResponse(PostWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["blogs"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Post",
        description="Update some fields of a specific post, only for `IsMarketing` or `IsAdministrator` users.",
        request=PostWriteSerializer,
        responses={
            200: OpenApiResponse(PostWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["blogs"],
    ),
    "destroy": extend_schema(
        summary="Remove a Post",
        description="Remove a specific post, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["blogs"],
    ),
    "create_report": extend_schema(
        summary="Create a Report for Post",
        description="Create a report of a post, only for `IsClient` or `IsAdministrator` users.",
        request=PostReportWriteSerializer,
        responses={
            201: OpenApiResponse(description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["blogs"],
    ),
    "get_reports": extend_schema(
        summary="Get all reports of Posts",
        description="Get a list of all available posts, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(PostReportReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["blogs"],
    ),
    "get_featured_posts": extend_schema(
        summary="Get all Featured Posts",
        description="Get a list of all featured posts.",
        responses={
            200: OpenApiResponse(PostReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["blogs"],
    ),
    "get_recent_posts": extend_schema(
        summary="Get all Recent Posts",
        description="Get a list of recent posts.",
        responses={
            200: OpenApiResponse(PostReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["blogs"],
    ),
    "get_tags": extend_schema(
        summary="Get all Tags for Posts",
        description="Get a list of tags for posts.",
        responses={
            200: OpenApiResponse(TagReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["blogs"],
    ),
    "create_tag": extend_schema(
        summary="Create a Tag for Post",
        description="Create a tag of a post, only for `IsMarketing` or `IsAdministrator` users.",
        request=TagWriteSerializer,
        responses={
            201: OpenApiResponse(TagWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["blogs"],
    ),
}
