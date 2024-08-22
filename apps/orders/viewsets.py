"""ViewSets for Orders App."""

from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsOwner, IsClient, IsDriver, IsDispatcher
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.utilities.helpers import generate_response
from apps.drivers.services import DriverService
from apps.deliveries.services import DeliveryService
from apps.deliveries.models import Delivery
from apps.deliveries.serializers import FailedDeliverySerializer, SignatureSerializer
from apps.deliveries.choices import StatusChoices
from .models import Order, OrderItem, OrderReport
from .services import OrderService
from .serializers import (
    OrderReadSerializer,
    OrderWriteSerializer,
    OrderMinimalSerializer,
    OrderItemReadSerializer,
    OrderItemWriteSerializer,
    OrderReportWriteSerializer,
    OrderRatingWriteSerializer,
)
from .schemas import order_schemas, order_item_schemas


@extend_schema_view(**order_schemas)
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
        if getattr(self, "swagger_fake_view", False):
            return Order.objects.none()

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
        methods=["post"],
        detail=True,
        url_path="report",
        permission_classes=[IsClient],
    )
    def report_order(self, request, *args, **kwargs):
        """
        Action report a specific order by ID.

        Endpoints:
        - POST api/v1/orders/{id}/report/
        """
        order = self.get_object()
        serializer = OrderReportWriteSerializer(data=request.data)
        if serializer.is_valid():
            if OrderReport.objects.filter(
                order_id=order, user_id=request.user
            ).exists():
                return Response(
                    {"error": "You have already reported this order."},
                    status=status.HTTP_409_CONFLICT,
                )
            serializer.save(order_id=order, user_id=request.user)
            return Response(
                {"detail": "Your report has been submitted successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        methods=["patch"],
        detail=True,
        url_path="asign_driver",
        permission_classes=[IsDispatcher],
    )
    def assign_driver(self, request, *args, **kwargs):
        """
        Action assign an available driver to a specific order.

        Endpoints:
        - PATCH api/v1/orders/{id}/asign_driver/
        """
        order = self.get_object()
        result = DriverService.assign_driver_to_order(order)
        return generate_response(result)

        # available_drivers = Driver.objects.get_available().filter(
        #     is_verified=True, is_active=True
        # )

        # if not available_drivers.exists():
        #     return Response(
        #         {"error": "There are no drivers available for assignment."},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )

        # driver = random.choice(available_drivers)
        # DriverAssignment.objects.create(order_id=order, driver_id=driver)

        # return Response(
        #     {"detail": f"Driver {driver.id} assigned to order {order.id}."},
        #     status=status.HTTP_200_OK,
        # )

    @action(
        methods=["patch"],
        detail=True,
        url_path="accept",
        permission_classes=[IsDriver],
    )
    def accept_order(self, request, *args, **kwargs):
        """
        Action to mark a specific order assignment as accepted.

        Endpoints:
        - POST api/v1/orders/{id}/accept/
        """
        order = self.get_object()
        driver = request.user.driver
        result = OrderService.accept_order(order, driver)
        return generate_response(result)

    @action(
        methods=["patch"],
        detail=True,
        url_path="reject",
        permission_classes=[IsDriver],
    )
    def reject_order(self, request, *args, **kwargs):
        """
        Action to mark a specific order assignment as rejected.

        Endpoints:
        - PATCH api/v1/orders/{id}/reject/
        """
        order = self.get_object()
        driver = request.user.driver
        result = OrderService.reject_order(order, driver)
        return generate_response(result)

    @action(
        methods=["patch"],
        detail=True,
        url_path="picked_up",
        permission_classes=[IsDriver],
    )
    def picked_up_order(self, request, *args, **kwargs):
        """
        Action to mark a delivery status to pickup.

        Endpoints:
        - PATCH api/v1/orders/{id}/picked_up/
        """
        order = self.get_object()
        driver = request.user.driver
        result = DeliveryService.mark_as_picked_up(order, driver)
        return generate_response(result)

    @action(
        methods=["post"],
        detail=True,
        url_path="delivered",
        permission_classes=[IsDriver],
    )
    def delivered_order(self, request, *args, **kwargs):
        """
        Action to mark a delivery status to delivered.

        Endpoints:
        - POST api/v1/orders/{id}/delivered/
        """
        order = self.get_object()
        driver = request.user.driver

        serializer = SignatureSerializer(data=request.data)
        if serializer.is_valid():
            signature = serializer.validated_data["signature"]
            result = DeliveryService.mark_as_delivered(order, driver, signature)
            return generate_response(result)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        methods=["post"],
        detail=True,
        url_path="failed",
        permission_classes=[IsDriver],
    )
    def failed_order(self, request, *args, **kwargs):
        """
        Action to mark a delivery status to failed.

        Endpoints:
        - POST api/v1/orders/{id}/failed/
        """
        order = self.get_object()
        driver = request.user.driver

        delivery = Delivery.objects.get(
            order_id=order,
            driver_id=driver,
        )

        if delivery.status in [StatusChoices.ASSIGNED, StatusChoices.PICKED_UP]:
            serializer = FailedDeliverySerializer(data=request.data)
            if serializer.is_valid():
                reason = serializer.validated_data["reason"]

                DeliveryService.record_failed_delivery(order, driver, reason)
                # TODO: Add notifications service
                return Response(
                    {"detail": "Failed delivery recorded successfully."},
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {"error": "The status could not be changed, please try again."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(
        methods=["post"],
        detail=True,
        url_path="rate",
        permission_classes=[IsClient],
    )
    def rate_order(self, request, *args, **kwargs):
        """
        Action for rate an order.

        Endpoints:
        - POST api/v1/orders/{id}/rate/
        """
        order = self.get_object()
        user = request.user

        serializer = OrderRatingWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(order_id=order, user_id=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**order_item_schemas)
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
        if getattr(self, "swagger_fake_view", False):
            return OrderItem.objects.none()
        # ! TODO: Add managers and optimize queries
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

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"error": "The combination of order and food already exists."},
                status=status.HTTP_400_BAD_REQUEST,
            )
