"""ViewSets for Drivers App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.users.permissions import IsSupport, IsClient, IsDriver, IsOwner
from apps.orders.models import Order
from apps.orders.serializers import OrderMinimalSerializer
from apps.deliveries.models import Delivery
from .models import Driver, Resource
from .services import DriverService
from .serializers import (
    DriverReadSerializer,
    DriverWriteSerializer,
    DriverMinimalSerializer,
    ResourceWriteSerializer,
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

    permission_classes = [IsSupport, IsOwner]
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
        detail=False,
        methods=["get"],
        permission_classes=[IsDriver],
        url_path="profile",
    )
    def get_profile(self, request, *args, **kwargs):
        """
        Action retrieve a driver profile.

        Endpoints:
        - GET api/v1/driver/profile/
        """
        driver = Driver.objects.get(user_id=request.user)
        if driver.is_available:
            serializer = DriverReadSerializer(driver)
            return Response(serializer.data)
        return Response(
            {"error": "Your profile has been deactivated."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[IsDriver],
        url_path="earnings",
    )
    def get_earnings(self, request, *args, **kwargs):
        """
        Action returns a list of earnings for a driver.

        Endpoints:
        - GET api/v1/driver/{id}/earnings/
        """
        try:
            driver = self.get_object()
            total_earnings = DriverService.calculate_earnings(driver)

            data = {
                "driver_name": driver.user_id.username,
                "total_earnings": total_earnings,
            }
            return Response(data, status=status.HTTP_200_OK)
        except Driver.DoesNotExist:
            return Response(
                {"error": "Driver not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsDriver],
        url_path="request_resources",
    )
    def request_resources(self, request, *args, **kwargs):
        """
        Action for requesting resources.

        Endpoints:
        - POST api/v1/resources/request/
        """
        driver = self.get_object()

        # Check if a previous request already exists
        if Resource.objects.filter(
            driver_id=driver,
            resource_type=request.data.get("resource_type"),
        ).exists():
            return Response(
                {"error": "You have already requested this resource."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create and validate the request
        serializer = ResourceWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(driver_id=driver)
        return Response(
            {"detail": "Request successful."}, status=status.HTTP_201_CREATED
        )

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

    @action(
        methods=["patch"],
        detail=True,
        url_path="verify",
        permission_classes=[IsSupport],
    )
    def verify_driver(self, request, *args, **kwargs):
        """
        Action to verify a newly registered driver.

        Endpoints:
        - PATCH api/v1/drivers/{id}/verify/
        """
        driver = self.get_object()

        try:
            return DriverService.verify_driver(driver)
        except Exception as e:
            return Response(
                {"detail": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
