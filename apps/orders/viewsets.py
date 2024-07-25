"""ViewSets for Orders App."""

from rest_framework.viewsets import ModelViewSet

from apps.users.permissions import IsOperations, IsClient
from apps.users.choices import RoleChoices
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Order
from .serializers import (
    OrderReadSerializer,
    OrderWriteSerializer,
    OrderMinimalSerializer,
)


class OrderViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Order instances.

    Endpoints:
    - GET /api/v1/orders/
    - POST /api/v1/orders/
    - GET /api/v1/orders/{id}/
    - PUT /api/v1/orders/{id}/
    - PATCH /api/v1/orders/{id}/
    - DELETE /api/v1/orders/{id}/
    """

    permission_classes = [IsOperations]
    serializer_class = OrderWriteSerializer
    search_fields = ["transaction", "shipping_name"]
    # filterset_class = OrderFilter

    def get_queryset(self):
        user = self.request.user

        if self.action == "list":
            if user.role in [RoleChoices.OPERATIONS, RoleChoices.ADMINISTRATOR]:
                return (
                    Order.objects.get_available()
                    .select_related(
                        "user_id",
                        "city_id",
                        "state_id",
                        "country_id",
                        "restaurant_id",
                    )
                    .only(
                        "id",
                        "shipping_name",
                        "transaction",
                        "restaurant_id",
                        "amount",
                        "status",
                        "updated_at",
                        "created_at",
                    )
                )
            elif user.role == RoleChoices.CLIENT:
                return (
                    Order.objects.get_available()
                    .filter(user_id=user)
                    .select_related(
                        "user_id",
                        "city_id",
                        "state_id",
                        "country_id",
                        "restaurant_id",
                    )
                    .only(
                        "id",
                        "shipping_name",
                        "transaction",
                        "restaurant_id",
                        "amount",
                        "status",
                        "updated_at",
                        "created_at",
                    )
                )
        else:
            if user.role in [RoleChoices.OPERATIONS, RoleChoices.ADMINISTRATOR]:
                return Order.objects.get_available().select_related(
                    "user_id",
                    "city_id",
                    "state_id",
                    "country_id",
                    "restaurant_id",
                )
            elif user.role == RoleChoices.CLIENT:
                return (
                    Order.objects.get_available()
                    .filter(user_id=user)
                    .select_related(
                        "user_id",
                        "city_id",
                        "state_id",
                        "country_id",
                        "restaurant_id",
                    )
                )

    # ! TODO: Add managers

    def get_serializer_class(self):
        if self.action == "list":
            return OrderMinimalSerializer
        elif self.action == "retrieve":
            return OrderReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsClient()]  # ! TODO: Add IsOwner and refactor
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
