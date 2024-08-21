"""Viewsets for Restaurant App."""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsPartner, IsClient, IsSupport
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.orders.models import Order
from apps.orders.serializers import OrderReadSerializer
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer, ReviewWriteSerializer
from .models import Restaurant, Category, Food
from .serializers import (
    RestaurantReadSerializer,
    RestaurantWriteSerializer,
    RestaurantMinimalSerializer,
    CategoryReadSerializer,
    CategoryWriteSerializer,
    CategoryMinimalSerializer,
    FoodReadSerializer,
    FoodWriteSerializer,
    FoodMinimalSerializer,
)
from .filters import RestaurantFilter
from .schemas import (
    restaurant_schemas,
    category_schemas,
    food_schemas,
    restaurant_review_schemas,
)


@extend_schema_view(**restaurant_schemas)
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


@extend_schema_view(**category_schemas)
class CategoryViewSet(ModelViewSet):
    """
    ViewSet for Category model.

    Endpoints:
    - GET /api/v1/restaurants/categories/
    - POST /api/v1/restaurants/categories/
    - GET /api/v1/restaurants/{id}/categories/{id}/
    - PUT /api/v1/restaurants/{id}/categories/{id}/
    - PATCH /api/v1/restaurants/{id}/categories/{id}/
    - DELETE /api/v1/restaurants/{id}/categories/{id}/
    """

    permission_classes = [IsPartner]
    serializer_class = CategoryWriteSerializer
    search_fields = ["name"]

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Category.objects.none()
        # ! TODO: Add managers and optimize queries
        if self.action == "list":
            return Category.objects.filter(
                restaurant_id=self.kwargs["restaurant_pk"], is_available=True
            ).values("id", "name")
        return Category.objects.filter(
            restaurant_id=self.kwargs["restaurant_pk"],
            is_available=True,
        ).select_related("restaurant_id")

    def get_serializer_class(self):
        if self.action == "list":
            return CategoryMinimalSerializer
        elif self.action == "retrieve":
            return CategoryReadSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        restaurant_id = self.kwargs["restaurant_pk"]
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        # Verify if the request user is the owner of the restaurant
        if restaurant.user_id != self.request.user:
            return Response(
                {
                    "error": "You do not have permission to add categories to this restaurant."
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        restaurant_id = self.kwargs["restaurant_pk"]
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        serializer.save(restaurant_id=restaurant)

    def update(self, request, *args, **kwargs):
        restaurant_id = self.kwargs["restaurant_pk"]
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        # Verify if the request user is the owner of the restaurant
        if restaurant.user_id != request.user:
            return Response(
                {"error": "You do not have permission to update this category."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        restaurant_id = self.kwargs["restaurant_pk"]
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        # Verify if the request user is the owner of the restaurant
        if restaurant.user_id != request.user:
            return Response(
                {"error": "You do not have permission to delete this category."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


@extend_schema_view(**food_schemas)
class FoodViewSet(ModelViewSet):
    """
    ViewSet for Food model.

    Endpoints:
    - GET /api/v1/restaurants/{id}/foods/
    - POST /api/v1/restaurants/{id}/foods/
    - GET /api/v1/restaurants/{id}/foods/{id}/
    - PUT /api/v1/restaurants/{id}/foods/{id}/
    - PATCH /api/v1/restaurants/{id}/foods/{id}/
    - DELETE /api/v1/restaurants/{id}/foods/{id}/
    """

    permission_classes = [IsPartner]
    serializer_class = FoodWriteSerializer
    search_fields = ["name"]
    # Filterset_class = FoodFilter

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Food.objects.none()
        # ! TODO: Add managers and optimize queries
        if self.action == "list":
            return Food.objects.filter(restaurant_id=self.kwargs["restaurant_pk"]).only(
                "id",
                "name",
                "price",
                "sale_price",
                "image",
                "category_id",
                "created_at",
                "updated_at",
            )
        return Food.objects.filter(
            restaurant_id=self.kwargs["restaurant_pk"]
        ).select_related("restaurant_id", "category_id")

    def get_serializer_class(self):
        if self.action == "list":
            return FoodMinimalSerializer
        elif self.action == "retrieve":
            return FoodReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        restaurant_id = self.kwargs["restaurant_pk"]
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        # Verify if the request user is the owner of the restaurant
        if restaurant.user_id != self.request.user:
            return Response(
                {
                    "error": "You do not have permission to add foods to this restaurant."
                },
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        restaurant_id = self.kwargs["restaurant_pk"]
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        serializer.save(restaurant_id=restaurant)

    def update(self, request, *args, **kwargs):
        restaurant_id = self.kwargs["restaurant_pk"]
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        # Verify if the request user is the owner of the restaurant
        if restaurant.user_id != request.user:
            return Response(
                {"error": "You do not have permission to update this food."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        restaurant_id = self.kwargs["restaurant_pk"]
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

        # Verify if the request user is the owner of the restaurant
        if restaurant.user_id != request.user:
            return Response(
                {"error": "You do not have permission to delete this food."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)


@extend_schema_view(**restaurant_review_schemas)
class RestaurantReviewViewSet(ModelViewSet):
    """
    ViewSet for RestaurantReview instances.

    Endpoints:
    - GET /api/v1/restaurants/{id}/reviews/
    - POST /api/v1/restaurants/{id}/reviews/
    - GET /api/v1/restaurants/{id}/reviews/{id}/
    - PUT /api/v1/restaurants/{id}/reviews/{id}/
    - PATCH /api/v1/restaurants/{id}/reviews/{id}/
    - DELETE /api/v1/restaurants/{id}/reviews/{id}/
    """

    permission_classes = [IsClient]
    serializer_class = ReviewWriteSerializer
    search_fields = ["user_id"]
    # Filterset_class = ReviewFilter

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return Review.objects.none()
        # ! TODO: Add managers and optimize queries
        return (
            Review.objects.filter(
                object_id=self.kwargs["restaurant_pk"],
                content_type__model="restaurant",
            )
            .select_related("content_type", "user_id")
            .order_by("-created_at")
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ReviewReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    def create(self, request, *args, **kwargs):
        if Review.objects.filter(
            user_id=request.user, object_id=self.kwargs["restaurant_pk"]
        ).exists():
            return Response(
                {"error": "Only one review per user is allowed."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        restaurant_model = ContentType.objects.get_for_model(Restaurant)
        serializer.save(
            user_id=self.request.user,
            object_id=self.kwargs["restaurant_pk"],
            content_type=restaurant_model,
        )

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user_id != request.user:
            return Response(
                {"detail": "You can only modify your own reviews."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user_id != request.user:
            return Response(
                {"detail": "You can only delete your own reviews."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)
