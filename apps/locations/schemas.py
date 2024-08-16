"""Schemas for Locations App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    CountryReadSerializer,
    CountryWriteSerializer,
    CountryMinimalSerializer,
    StateReadSerializer,
    StateWriteSerializer,
    StateMinimalSerializer,
    CityReadSerializer,
    CityWriteSerializer,
    CityMinimalSerializer,
)


country_schemas = {
    "list": extend_schema(
        summary="Get Several Countries",
        description="Get a list of all available countries.",
        responses={
            200: OpenApiResponse(CountryMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["countries"],
    ),
    "create": extend_schema(
        summary="Create a Country",
        description="Create a new country, only for `IsAdministrator` users.",
        request=CountryWriteSerializer,
        responses={
            201: OpenApiResponse(CountryWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["countries"],
    ),
    "retrieve": extend_schema(
        summary="Get a Country",
        description="Get detailed information about a specific country.",
        responses={
            200: OpenApiResponse(CountryReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["countries"],
    ),
    "update": extend_schema(
        summary="Update a Country",
        description="Update all fields of a specific country, only for `IsAdministrator` users.",
        request=CountryWriteSerializer,
        responses={
            200: OpenApiResponse(CountryWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["countries"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Country",
        description="Update some fields of a specific country, only for `IsAdministrator` users.",
        request=CountryWriteSerializer,
        responses={
            200: OpenApiResponse(CountryWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["countries"],
    ),
    "destroy": extend_schema(
        summary="Remove a Country",
        description="Remove a specific country, only for `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["countries"],
    ),
}


state_schemas = {
    "list": extend_schema(
        summary="Get Several States",
        description="Get a list of all available states.",
        responses={
            200: OpenApiResponse(StateMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["states"],
    ),
    "create": extend_schema(
        summary="Create a State",
        description="Create a new state, only for `IsAdministrator` users.",
        request=StateWriteSerializer,
        responses={
            201: OpenApiResponse(StateWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["states"],
    ),
    "retrieve": extend_schema(
        summary="Get a State",
        description="Get detailed information about a specific state.",
        responses={
            200: OpenApiResponse(StateReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["states"],
    ),
    "update": extend_schema(
        summary="Update a State",
        description="Update all fields of a specific state, only for `IsAdministrator` users.",
        request=StateWriteSerializer,
        responses={
            200: OpenApiResponse(StateWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["states"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a State",
        description="Update some fields of a specific state, only for `IsAdministrator` users.",
        request=StateWriteSerializer,
        responses={
            200: OpenApiResponse(StateWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["states"],
    ),
    "destroy": extend_schema(
        summary="Remove a State",
        description="Remove a specific state, only for `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["states"],
    ),
}


city_schemas = {
    "list": extend_schema(
        summary="Get Several Cities",
        description="Get a list of all available cities.",
        responses={
            200: OpenApiResponse(CityMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["cities"],
    ),
    "create": extend_schema(
        summary="Create a City",
        description="Create a new city, only for `IsAdministrator` users.",
        request=CityWriteSerializer,
        responses={
            201: OpenApiResponse(CityWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["cities"],
    ),
    "retrieve": extend_schema(
        summary="Get a City",
        description="Get detailed information about a specific city.",
        responses={
            200: OpenApiResponse(CityReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["cities"],
    ),
    "update": extend_schema(
        summary="Update a City",
        description="Update all fields of a specific city, only for `IsAdministrator` users.",
        request=CityWriteSerializer,
        responses={
            200: OpenApiResponse(CityWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["cities"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a City",
        description="Update some fields of a specific city, only for `IsAdministrator` users.",
        request=CityWriteSerializer,
        responses={
            200: OpenApiResponse(CityWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["cities"],
    ),
    "destroy": extend_schema(
        summary="Remove a City",
        description="Remove a specific city, only for `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["cities"],
    ),
}
