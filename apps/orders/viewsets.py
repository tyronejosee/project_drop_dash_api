"""ViewSets for Orders App."""

import random
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsOwner, IsClient, IsDriver, IsDispatcher
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.drivers.models import Driver, DriverAssignment
from apps.drivers.choices import AssignmentStatusChoices
from apps.deliveries.models import Delivery, FailedDelivery
from apps.deliveries.serializers import FailedDeliverySerializer, SignatureSerializer
from apps.deliveries.choices import StatusChoices
from .models import Order, OrderItem, OrderReport
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
        Pending.

        Endpoints:
        - PATCH api/v1/orders/{id}/asign_driver/
        """
        order = self.get_object()
        available_drivers = Driver.objects.get_available().filter(
            is_verified=True, is_active=True
        )
        # ! TODO: Add location filter and manager

        if not available_drivers.exists():
            return Response(
                {"error": "There are no drivers available for assignment."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        driver = random.choice(available_drivers)
        DriverAssignment.objects.create(order_id=order, driver_id=driver)

        return Response(
            {"detail": f"Driver {driver.id} assigned to order {order.id}."},
            status=status.HTTP_200_OK,
        )

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
        try:
            # ! TODO: Add service layer
            order = self.get_object()
            driver = request.user.driver

            assignment = DriverAssignment.objects.filter(
                is_available=True,
                driver_id=driver,
                status=AssignmentStatusChoices.PENDING,
            ).first()
            assignment.status = AssignmentStatusChoices.ACCEPTED
            assignment.is_available = False
            assignment.save()

            # Create delivery entries
            Delivery.objects.create(
                order_id=order,
                driver_id=driver,
                status=StatusChoices.ASSIGNED,
            )

            return Response(
                {"detail": f"The order {order} was accepted."},
                status=status.HTTP_200_OK,
            )
        except DriverAssignment.DoesNotExist:
            return Response(
                {"error": "No pending assignment found for this driver."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": f"{e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

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
        try:
            # ! TODO: Add service layer
            order = self.get_object()
            driver = request.user.driver

            assignment = DriverAssignment.objects.get(
                driver_id=driver,
                order_id=order,
            )
            assignment.status = AssignmentStatusChoices.REJECTED
            assignment.is_available = False
            assignment.save()
            return Response(
                {"detail": f"The order {order} was rejected."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": f"{e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

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

        delivery = Delivery.objects.get(
            order_id=order,
            driver_id=driver,
        )
        # ! TODO: Add service layer
        if delivery.status == StatusChoices.ASSIGNED:
            delivery.status = StatusChoices.PICKED_UP
            delivery.picked_up_at = timezone.now()
            delivery.save()
            return Response(
                {"detail": "Delivery status was changed to 'Picked Up'."},
                status=status.HTTP_200_OK,
            )
        elif delivery.status == StatusChoices.PICKED_UP:
            return Response(
                {"error": "Delivery has already been marked as 'Picked Up'."},
                status=status.HTTP_409_CONFLICT,
            )
        return Response(
            {"error": "Delivery with status pending cannot be marked."},
            status=status.HTTP_400_BAD_REQUEST,
        )

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

            delivery = Delivery.objects.get(
                order_id=order,
                driver_id=driver,
            )

            if delivery.status == StatusChoices.PICKED_UP:
                # TODO: Add verification code
                delivery.signature = signature
                delivery.status = StatusChoices.DELIVERED
                delivery.delivered_at = timezone.now()
                delivery.is_completed = True
                delivery.save()

                return Response(
                    {"detail": "Order successfully delivered."},
                    status=status.HTTP_200_OK,
                )
            return Response(
                {"error": "The status could not be changed, please try again."},
                status=status.HTTP_409_CONFLICT,
            )
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
                # Record failed delivery
                FailedDelivery.objects.create(
                    order_id=order,
                    driver_id=driver,
                    reason=reason,
                    failed_at=timezone.now(),
                )  # ! TODO: Add services layer

                delivery.status = StatusChoices.FAILED
                delivery.save()
                # TODO: Add notifications
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
        # TODO: Refactor this

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
