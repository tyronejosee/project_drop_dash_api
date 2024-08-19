"""ViewSets for Jobs App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsHumanResources
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Position, Worker, Applicant
from .services import WorkerService
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
from .filters import WorkerFilter, ApplicantFilter
from .schemas import position_schemas, worker_schemas, applicant_schemas


@extend_schema_view(**position_schemas)
class PositionViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Position instances.

    Endpoints:
    - GET /api/v1/positions/
    - POST /api/v1/positions/
    - GET /api/v1/positions/{id}/
    - PUT /api/v1/positions/{id}/
    - PATCH /api/v1/positions/{id}/
    - DELETE /api/v1/positions/{id}/
    """

    permission_classes = [IsHumanResources]
    serializer_class = PositionWriteSerializer
    search_fields = ["position"]

    def get_queryset(self):
        if self.action == "list":
            return Position.objects.get_list()
        return Position.objects.get_available()

    def get_serializer_class(self):
        if self.action == "list":
            return PositionMinimalSerializer
        elif self.action == "retrieve":
            return PositionReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()


@extend_schema_view(**worker_schemas)
class WorkerViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Worker instances.

    Endpoints:
    - GET /api/v1/workers/
    - POST /api/v1/workers/
    - GET /api/v1/workers/{id}/
    - PUT /api/v1/workers/{id}/
    - PATCH /api/v1/workers/{id}/
    - DELETE /api/v1/workers/{id}/
    """

    permission_classes = [IsHumanResources]
    serializer_class = WorkerWriteSerializer
    search_fields = ["user_id", "contract_type"]
    filterset_class = WorkerFilter

    def get_queryset(self):
        # ! TODO: Perfom queries
        return Worker.objects.get_available()

    def get_serializer_class(self):
        if self.action == "list":
            return WorkerMinimalSerializer
        elif self.action == "retrieve":
            return WorkerReadSerializer
        return super().get_serializer_class()

    @action(
        methods=["patch"],
        detail=True,
        url_path="terminate",
        permission_classes=[IsHumanResources],
    )
    def terminate_contract(self, request, *args, **kwargs):
        """
        Action changes the contract status of a worker.

        Endpoints:
        - PATCH api/v1/drivers/{id}/verify/
        """
        worker = self.get_object()
        WorkerService.terminate_worker(worker)
        return Response(
            {"detail": "Contract terminated, worker disengaged."},
            status=status.HTTP_200_OK,
        )


@extend_schema_view(**applicant_schemas)
class ApplicantViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Applicant instances.

    Endpoints:
    - GET /api/v1/applicants/
    - POST /api/v1/applicants/
    - GET /api/v1/applicants/{id}/
    - PUT /api/v1/applicants/{id}/
    - PATCH /api/v1/applicants/{id}/
    - DELETE /api/v1/applicants/{id}/
    """

    permission_classes = [IsHumanResources]
    serializer_class = ApplicantWriteSerializer
    search_fields = ["user_id", "contract_type"]
    filterset_class = ApplicantFilter

    def get_queryset(self):
        return Applicant.objects.get_available()

    def get_serializer_class(self):
        if self.action == "list":
            return ApplicantMinimalSerializer
        elif self.action == "retrieve":
            return ApplicantReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["create"]:
            return [AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
