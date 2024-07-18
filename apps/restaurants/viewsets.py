"""Viewsets for Restaurant App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsPartner
from apps.utils.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.orders.models import Order
from apps.orders.serializers import OrderReadSerializer
from .models import Restaurant
from .serializers import (
    RestaurantReadSerializer,
    RestaurantWriteSerializer,
    RestaurantListSerializer,
)


class RestaurantViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Restaurant instances.

    Endpoints:
    - GET /api/v1/restaurants/
    - POST /api/v1/restaurants/
    - GET /api/v1/restaurants/{id}/
    - PUT /api/v1/restaurants/{id}/
    - PATCH /api/v1/restaurants/{id}/
    - DELETE /api/v1/restaurants/{id}/
    """

    permission_classes = [IsPartner]
    serializer_class = RestaurantWriteSerializer
    search_fields = ["name"]
    # filterset_class = RestaurantFilter

    def get_queryset(self):
        return Restaurant.objects.get_available()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return RestaurantListSerializer
        elif self.action == "retrieve":
            return RestaurantReadSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="orders",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_orders(self, request, *args, **kwargs):
        restaurant = self.get_object()
        orders = Order.objects.filter(restaurant=restaurant)
        if orders.exists():
            serializer = OrderReadSerializer(orders, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No orders found for this restaurant."},
            status=status.HTTP_404_NOT_FOUND,
        )
