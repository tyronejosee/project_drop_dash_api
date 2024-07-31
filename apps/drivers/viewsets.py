"""ViewSets for Drivers App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.users.permissions import IsSupport, IsClient, IsDriver
from apps.orders.models import Order
from apps.orders.serializers import OrderMinimalSerializer
from apps.deliveries.models import Delivery
from .models import Driver
from .services import DriverService
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

    def get_queryset(self):
        if self.action == "list":
            Driver.objects.get_list()
        return Driver.objects.get_detail()

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

    def create(self, request, *args, **kwargs):
        return DriverService.create_driver(request.user, request.data)

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[IsDriver],
        url_path="earnings",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_earnings(self, request, *args, **kwargs):
        """
        Action returns a list of earnings for a driver.

        Endpoints:
        - GET api/v1/driver/{id}/earnings/
        """
        pass

    # ! TODO: Pending implementation

    @action(
        detail=True,
        methods=["patch"],
        permission_classes=[IsDriver],
        url_path="availability",
    )
    def toggle_availability(self, request, *args, **kwargs):
        """
        Action changes the availability status of a driver.

        Endpoints:
        - GET api/v1/driver/{id}/availability/
        """

        driver = self.get_object()

        if driver.user_id != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )

        is_active = DriverService.toggle_availability(driver)
        message = "ONLINE" if is_active else "OFFLINE"
        return Response(
            {"detail": f"Status driver {message}"},
            status=status.HTTP_200_OK,
        )

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[IsDriver],
        url_path="orders",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_orders(self, request, *args, **kwargs):
        """
        Action returns a list of orders for a driver.

        Endpoints:
        - GET api/v1/driver/{id}/orders/
        """
        driver = self.get_object()

        relations = Delivery.objects.filter(driver_id=driver)
        if not relations.exists():
            return Response(
                {"detail": "No orders found for this driver."},
                status=status.HTTP_404_NOT_FOUND,
            )

        order_ids = relations.values_list("order_id", flat=True)
        orders = Order.objects.filter(id__in=order_ids)

        if not orders.exists():
            return Response(
                {"detail": "No orders found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = OrderMinimalSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
