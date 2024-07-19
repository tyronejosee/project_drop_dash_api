"""Viewsets for Restaurant App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsPartner, IsClient, IsSupport
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.orders.models import Order
from apps.orders.serializers import OrderReadSerializer
from .models import Restaurant, Category
from .serializers import (
    RestaurantReadSerializer,
    RestaurantWriteSerializer,
    RestaurantMinimalSerializer,
    CategoryMinimalSerializer,
)
from .filters import RestaurantFilter


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
    filterset_class = RestaurantFilter

    def get_queryset(self):
        return Restaurant.objects.get_verified()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        elif self.action == "create":
            return [IsClient()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "list":
            return RestaurantMinimalSerializer
        elif self.action == "retrieve":
            return RestaurantReadSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[IsPartner],
        url_path="orders",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_orders(self, request, *args, **kwargs):
        """
        Action retrieve orders associated with a restaurant.

        Endpoints:
        - GET api/v1/restaurants/{id}/orders/
        """
        restaurant = self.get_object()
        orders = Order.objects.filter(restaurant_id=restaurant)
        if orders.exists():
            serializer = OrderReadSerializer(orders, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No orders found for this restaurant."},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=True,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="categories",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_categories(self, request, *args, **kwargs):
        """
        Action retrieve categories associated with a restaurant.

        Endpoints:
        - GET api/v1/restaurants/{id}/categories/
        """
        restaurant = self.get_object()
        categories = Category.objects.filter(restaurant_id=restaurant)
        if categories.exists():
            serializer = CategoryMinimalSerializer(categories, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No categories found for this restaurant."},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsSupport],
        url_path="pending-verification",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_pending_verification(self, request, *args, **kwargs):
        """
        Action retrieve restaurants pending verification.

        Endpoints:
        - GET api/v1/restaurants/pending-verification/
        """
        restaurants = Restaurant.objects.get_unverified()
        if restaurants.exists():
            serializer = RestaurantReadSerializer(restaurants, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No restaurants found."},
            status=status.HTTP_404_NOT_FOUND,
        )
