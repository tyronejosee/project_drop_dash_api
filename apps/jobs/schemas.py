"""Schemas for Jobs App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from .serializers import (
    PositionReadSerializer,
    PositionWriteSerializer,
    PositionMinimalSerializer,
    WorkerReadSerializer,
    WorkerWriteSerializer,
    WorkerMinimalSerializer,
    ApplicantReadSerializer,
    ApplicantWriteSerializer,
    ApplicantMinimalSerializer,
)


position_schemas = {
    "list": extend_schema(
        summary="Get Several Positions",
        description="Get a list of all available positions.",
        responses={
            200: OpenApiResponse(
                PositionMinimalSerializer(many=True), description="OK"
            ),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["positions"],
    ),
    "create": extend_schema(
        summary="Create a Position",
        description="Create a new position, only for `IsHumanResources` or `IsAdministrator` users.",
        request=PositionWriteSerializer,
        responses={
            201: OpenApiResponse(PositionWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["positions"],
    ),
    "retrieve": extend_schema(
        summary="Get a Position",
        description="Get detailed information about a specific position.",
        responses={
            200: OpenApiResponse(PositionReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["positions"],
    ),
    "update": extend_schema(
        summary="Update a Position",
        description="Update all fields of a specific position, only for `IsHumanResources` or `IsAdministrator` users.",
        request=PositionWriteSerializer,
        responses={
            200: OpenApiResponse(PositionWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["positions"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Position",
        description="Update some fields of a specific position, only for `IsHumanResources` or `IsAdministrator` users.",
        request=PositionWriteSerializer,
        responses={
            200: OpenApiResponse(PositionWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["positions"],
    ),
    "destroy": extend_schema(
        summary="Remove a Position",
        description="Remove a specific position, only for `IsHumanResources` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["positions"],
    ),
}


worker_schemas = {
    "list": extend_schema(
        summary="Get Several Workers",
        description="Get a list of all available workers.",
        responses={
            200: OpenApiResponse(WorkerMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["workers"],
    ),
    "create": extend_schema(
        summary="Create a Worker",
        description="Create a new worker, only for `IsHumanResources` or `IsAdministrator` users.",
        request=WorkerWriteSerializer,
        responses={
            201: OpenApiResponse(WorkerWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["workers"],
    ),
    "retrieve": extend_schema(
        summary="Get a Worker",
        description="Get detailed information about a specific worker.",
        responses={
            200: OpenApiResponse(WorkerReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["workers"],
    ),
    "update": extend_schema(
        summary="Update a Worker",
        description="Update all fields of a specific worker, only for `IsHumanResources` or `IsAdministrator` users.",
        request=WorkerWriteSerializer,
        responses={
            200: OpenApiResponse(WorkerWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["workers"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Worker",
        description="Update some fields of a specific worker, only for `IsHumanResources` or `IsAdministrator` users.",
        request=WorkerWriteSerializer,
        responses={
            200: OpenApiResponse(WorkerWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["workers"],
    ),
    "destroy": extend_schema(
        summary="Remove a Worker",
        description="Remove a specific worker, only for `IsHumanResources` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["workers"],
    ),
    "terminate_contract": extend_schema(
        summary="Terminate Contract of a Worker",
        description="Terminate Contract of a specific worker, only for `IsHumanResources` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(description="Contract terminated, worker disengaged."),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["workers"],
    ),
}


applicant_schemas = {
    "list": extend_schema(
        summary="Get Several Applicants",
        description="Get a list of all available applicants, only for `IsHumanResources` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(
                ApplicantMinimalSerializer(many=True), description="OK"
            ),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["applicants"],
    ),
    "create": extend_schema(
        summary="Create a Applicant",
        description="Create a new applicant.",
        request=ApplicantWriteSerializer,
        responses={
            201: OpenApiResponse(ApplicantWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        auth=[],
        tags=["applicants"],
    ),
    "retrieve": extend_schema(
        summary="Get a Applicant",
        description="Get detailed information about a specific applicant, only for `IsHumanResources` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(ApplicantReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["applicants"],
    ),
    "update": extend_schema(
        summary="Update a Applicant",
        description="Update all fields of a specific applicant, only for `IsHumanResources` or `IsAdministrator` users.",
        request=ApplicantWriteSerializer,
        responses={
            200: OpenApiResponse(ApplicantWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["applicants"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Applicant",
        description="Update some fields of a specific applicant, only for `IsHumanResources` or `IsAdministrator` users.",
        request=ApplicantWriteSerializer,
        responses={
            200: OpenApiResponse(ApplicantWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["applicants"],
    ),
    "destroy": extend_schema(
        summary="Remove a Applicant",
        description="Remove a specific applicant, only for `IsHumanResources` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["applicants"],
    ),
}
