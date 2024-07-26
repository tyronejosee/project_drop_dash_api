"""ViewSets for Orders App."""

from rest_framework.viewsets import ModelViewSet

from apps.users.permissions import IsOwner, IsClient
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

    permission_classes = [IsClient, IsOwner]
    serializer_class = OrderWriteSerializer
    search_fields = ["transaction", "shipping_name"]
    # filterset_class = OrderFilter

    def get_queryset(self):
        user = self.request.user
        if self.action == "list":
            return Order.objects.get_list_by_user(user)
        return Order.objects.get_detail_by_user(user)

    def get_serializer_class(self):
        if self.action == "list":
            return OrderMinimalSerializer
        elif self.action == "retrieve":
            return OrderReadSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
