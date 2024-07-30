"""ViewSets for Drivers App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from apps.utilities.functions import encrypt_field
from apps.users.permissions import IsSupport, IsClient
from apps.users.choices import RoleChoices
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Driver
from .serializers import (
    DriverReadSerializer,
    DriverWriteSerializer,
    DriverMinimalSerializer,
)


class DriverViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Driver instances.

    Endpoints:
    - GET /api/v1/drivers/
    - POST /api/v1/drivers/
    - GET /api/v1/drivers/{id}/
    - PUT /api/v1/drivers/{id}/
    - PATCH /api/v1/drivers/{id}/
    - DELETE /api/v1/drivers/{id}/
    """

    permission_classes = [IsSupport]
    serializer_class = DriverWriteSerializer
    search_fields = ["user_id"]
    # filterset_class = DriverFilter

    def create(self, request, *args, **kwargs):
        # Check if the user already has a driver profile
        if Driver.objects.filter(user_id=request.user).exists():
            return Response(
                {"detail": "This user already has a driver profile."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = DriverWriteSerializer(data=request.data)
        if serializer.is_valid():
            # Encrypt specific fields after they have been validated
            validated_data = serializer.validated_data
            validated_data["phone"] = encrypt_field(validated_data["phone"])
            validated_data["address"] = encrypt_field(validated_data["address"])
            serializer.save(user_id=request.user)

            request.user.role = RoleChoices.DRIVER  # Update role
            request.user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if self.action == "list":
            Driver.objects.get_available().select_related(
                "user_id", "city_id", "state_id", "country_id"
            ).only("id", "user_id", "city_id", "state_id", "country_id", "status")
        return Driver.objects.get_available()

    def get_serializer_class(self):
        if self.action == "list":
            return DriverMinimalSerializer
        elif self.action == "retrieve":
            return DriverReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsClient()]
        return super().get_permissions()
