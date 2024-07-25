"""ViewSets for Jobs App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from apps.users.permissions import IsHumanResources
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Position, Worker, Applicant
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
        return Worker.objects.get_available()

    def get_serializer_class(self):
        if self.action == "list":
            return WorkerMinimalSerializer
        elif self.action == "retrieve":
            return WorkerReadSerializer
        return super().get_serializer_class()


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
