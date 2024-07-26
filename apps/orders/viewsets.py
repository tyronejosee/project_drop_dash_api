"""ViewSets for Orders App."""

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from apps.users.permissions import IsOwner, IsClient
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Order, OrderItem
from .serializers import (
    OrderReadSerializer,
    OrderWriteSerializer,
    OrderMinimalSerializer,
    OrderItemReadSerializer,
    OrderItemWriteSerializer,
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


class OrderItemViewSet(ModelViewSet):
    """
    ViewSet for managing OrderItem instances.

    Endpoints:
    - GET /api/v1/orders/{id}/items/
    - POST /api/v1/orders/{id}/items/
    - GET /api/v1/orders/{id}/items/{pk}/
    - PUT /api/v1/orders/{id}/items/{pk}/
    - PATCH /api/v1/orders/{id}/items/{pk}/
    - DELETE /api/v1/orders/{id}/items/{pk}/
    """

    permission_classes = [IsClient]
    serializer_class = OrderItemWriteSerializer
    search_fields = ["food_id"]
    pagination_class = None
    # filterset_class = OrderItemFilter

    def get_queryset(self):
        return OrderItem.objects.filter(
            order_id=self.kwargs["order_pk"]
        ).select_related("order_id", "food_id")

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return OrderItemReadSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        order = get_object_or_404(Order, user_id=self.request.user)
        serializer.save(order_id=order)
