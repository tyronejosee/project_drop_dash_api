"""ViewSets for Orders App."""

from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsOwner, IsClient, IsDriver
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.deliveries.models import Delivery
from apps.deliveries.choices import StatusChoices
from .models import Order, OrderItem, OrderReport
from .serializers import (
    OrderReadSerializer,
    OrderWriteSerializer,
    OrderMinimalSerializer,
    OrderItemReadSerializer,
    OrderItemWriteSerializer,
    OrderReportWriteSerializer,
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

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsClient],
        url_path="report",
    )
    def report_order(self, request, *args, **kwargs):
        """
        Action report a specific order by ID.

        Endpoints:
        - GET api/v1/orders/{id}/report/
        """
        order = self.get_object()
        serializer = OrderReportWriteSerializer(data=request.data)
        if serializer.is_valid():
            if OrderReport.objects.filter(
                order_id=order, user_id=request.user
            ).exists():
                return Response(
                    {"detail": "You have already reported this order."},
                    status=status.HTTP_409_CONFLICT,
                )
            serializer.save(order_id=order, user_id=request.user)
            return Response(
                {"detail": "Your report has been submitted successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=True,
        methods=["patch"],
        permission_classes=[IsDriver],
        url_path="reject",
    )
    def reject_order(self, request, pk=None):
        """
        Action to mark a specific order report as rejected.
        TODO: Concept tests, temporal

        Endpoints:
        - PATCH api/v1/orders/{id}/reject/
        """
        order = self.get_object()
        delivery = Delivery.objects.get(order_id=order)

        if delivery:
            delivery.status = StatusChoices.FAILED
            delivery.save()
            return Response(
                {"detail": f"The order {order} was rejected."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": f"Order {order} not found."},
            status=status.HTTP_404_NOT_FOUND,
        )


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
