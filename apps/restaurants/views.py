"""Views for Restaurants App."""

import re
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view

from apps.orders.models import Order
from apps.orders.serializers import OrderReadSerializer
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer, ReviewWriteSerializer
from apps.users.permissions import IsPartner, IsClient
from apps.utilities.pagination import LargeSetPagination
from .models import Restaurant, Category, Food
from .serializers import (
    RestaurantReadSerializer,
    RestaurantWriteSerializer,
    CategoryReadSerializer,
    CategoryWriteSerializer,
    FoodReadSerializer,
    FoodWriteSerializer,
)
from .schemas import (
    restaurant_list_schema,
    restaurant_detail_schema,
    category_list_schema,
    category_detail_schema,
    food_list_schema,
    food_detail_schema,
)


@extend_schema_view(**restaurant_list_schema)
class RestaurantListView(APIView):
    """
    View to list and create restaurants.

    Endpoints:
    - GET api/v1/restaurants/
    - POST api/v1/restaurants/
    """

    permission_classes = [AllowAny]
    cache_key = "restaurant_list"

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsClient()]
        return super().get_permissions()

    def get(self, request):
        # Get a list of restaurants
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            restaurants = Restaurant.objects.get_available()
            if not restaurants.exists():
                return Response(
                    {"detail": "No restaurants available."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(restaurants, request)
            # Set cache
            cache.set(self.cache_key, paginated_data, 7200)
            serializer = RestaurantReadSerializer(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)

        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(cached_data, request)
            serializer = RestaurantReadSerializer(paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request):
        # Create a new restaurant
        serializer = RestaurantWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**restaurant_detail_schema)
class RestaurantDetailView(APIView):
    """
    View to retrieve, update, and delete a restaurant.

    Endpoints:
    - GET api/v1/restaurants/{id}/
    - PUT api/v1/restaurants/{id}/
    - DELETE api/v1/restaurants/{id}/
    """

    permission_classes = [IsPartner]

    def get_object(self, restaurant_id):
        # Get a restaurant instance by id
        return get_object_or_404(Restaurant, pk=restaurant_id)

    def get(self, request, restaurant_id):
        # Get details of a restaurant
        restaurant = self.get_object(restaurant_id)
        serializer = RestaurantReadSerializer(restaurant)
        return Response(serializer.data)

    @transaction.atomic
    def put(self, request, restaurant_id):
        # Update a restaurant
        restaurant = self.get_object(restaurant_id)
        serializer = RestaurantWriteSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, restaurant_id):
        # Delete a restaurant
        restaurant = self.get_object(restaurant_id)
        restaurant.is_available = False  # Logical deletion
        restaurant.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestaurantSearchView(APIView):
    """
    View to search restaurants.

    Endpoints:
    - GET api/v1/restaurants/search/?q=<search_term>
    """

    def get(self, request):
        # Search for promotions for name and conditions fields
        search_term = request.query_params.get("q", "")
        search_term = re.sub(r"[^\w\s\-\(\)\.,]", "", search_term).strip()

        if not search_term:
            return Response(
                {"detail": "No search query provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        restaurants = Restaurant.objects.get_search(search_term)

        if not restaurants.exists():
            return Response(
                {"detail": "No results found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = RestaurantReadSerializer(restaurants, many=True)
        return Response(serializer.data)


class RestaurantOrderListView(APIView):
    """
    View to retrieve orders for a specific restaurant.

    Endpoints:
    - GET api/v1/restaurants/{id}/orders/
    """

    def get(self, request, restaurant_id, format=None):
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        orders = Order.objects.filter(restaurant=restaurant)

        paginator = LargeSetPagination()
        page = paginator.paginate_queryset(orders, request)

        if page is not None:
            serializer = OrderReadSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = OrderReadSerializer(orders, many=True)
        return Response(serializer.data)


class RestaurantReviewListView(APIView):
    """
    View to list and create reviews for a restaurant

    Endpoints:
    - GET api/v1/restaurants/{id}/reviews/
    - POST api/v1/restaurants/{id}/reviews/
    """

    permission_classes = [IsClient]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return super().get_permissions()

    def get(self, request, restaurant_id):
        # List reviews for a restaurant
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        restaurant_content_type = ContentType.objects.get_for_model(Restaurant)

        reviews = Review.objects.filter(
            content_type=restaurant_content_type, object_id=restaurant.pk
        ).order_by("-created_at")

        serializer = ReviewReadSerializer(reviews, many=True)
        return Response(serializer.data)

    def post(self, request, restaurant_id):
        # Create a review for a restaurant.
        restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
        restaurant_content_type = ContentType.objects.get_for_model(Restaurant)
        serializer = ReviewWriteSerializer(data=request.data)

        if Review.objects.filter(
            user=request.user,
            content_type=restaurant_content_type,
            object_id=restaurant.pk,
        ).exists():
            return Response(
                {"detail": "Only one review per user is allowed."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if serializer.is_valid():
            serializer.save(
                user=request.user,
                content_type=restaurant_content_type,
                object_id=restaurant.pk,
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantReviewDetailView(APIView):
    """
    View for retrieving, updating, or deleting a review of a restaurant.

    Endpoints:
    - GET api/v1/restaurants/{id}/reviews/{id}/
    - PATCH api/v1/restaurants/{id}/reviews/{id}/
    - DELETE api/v1/restaurants/{id}/reviews/{id}/
    """

    permission_classes = [IsClient]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return super().get_permissions()

    def get(self, request, restaurant_id, review_id):
        # Retrieve a review of a restaurant
        review = get_object_or_404(Review, pk=review_id, object_id=restaurant_id)
        serializer = ReviewReadSerializer(review)
        return Response(serializer.data)

    def patch(self, request, restaurant_id, review_id):
        # Update a review of a restaurant
        review = get_object_or_404(Review, pk=review_id, object_id=restaurant_id)

        if review.user != request.user:
            return Response(
                {"detail": "You can only modify or delete your own reviews."},
                status=status.HTTP_403_FORBIDDEN,
            )

        serializer = ReviewWriteSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant_id, review_id):
        # Remove a review of a restaurant
        review = get_object_or_404(Review, pk=review_id, object_id=restaurant_id)

        if review.user != request.user:
            return Response(
                {"detail": "You can only delete your own reviews."},
                status=status.HTTP_403_FORBIDDEN,
            )

        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(**category_list_schema)
class CategoryListView(APIView):
    """
    View to list and create categories.

    Endpoints:
    - GET api/v1/restaurants/{id}/categories/
    - POST api/v1/restaurants/{id}/categories/
    """

    permission_classes = [IsPartner]
    cache_key = "category_list"

    def get(self, request, restaurant_id, format=None):
        # Get a list of categories
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            categories = Category.objects.get_by_restaurant(restaurant_id)
            if not categories.exists():
                return Response(
                    {"detail": "No categories available."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(categories, request)
            serializer = CategoryReadSerializer(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, 7200)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(cached_data, request)
            serializer = CategoryReadSerializer(paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, restaurant_id, format=None):
        # Create a new category
        serializer = CategoryWriteSerializer(data=request.data)
        if serializer.is_valid():
            restaurant = get_object_or_404(Restaurant, id=restaurant_id)
            serializer.save(restaurant=restaurant)
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**category_detail_schema)
class CategoryDetailView(APIView):
    """
    View to retrieve, update, and delete a category.

    Endpoints:
    - GET api/v1/restaurants/{id}/categories/{id}/
    - PUT api/v1/restaurants/{id}/categories/{id}/
    - DELETE api/v1/restaurants/{id}/categories/{id}/
    """

    permission_classes = [IsPartner]

    def get_object(self, category_id):
        # Get a category instance by id
        return get_object_or_404(Category, pk=category_id)

    def get(self, request, restaurant_id, category_id):
        # Get details of a category
        category = self.get_object(category_id)
        serializer = CategoryReadSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, restaurant_id, category_id):
        # Update a category
        category = self.get_object(category_id)
        serializer = CategoryWriteSerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant_id, category_id):
        # Delete a category
        category = self.get_object(category_id)
        category.is_available = False  # Logical deletion
        category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(**food_list_schema)
class FoodListView(APIView):
    """
    View to list and create foods.

    Endpoints:
    - GET api/v1/restaurants/{id}/foods/
    - POST api/v1/restaurants/{id}/foods/
    """

    permission_classes = [AllowAny]
    cache_key = "food_list"

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsPartner()]
        return super().get_permissions()

    def get(self, request, restaurant_id, format=None):
        # Get a list of foods
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            foods = Food.objects.get_foods_by_restaurant(restaurant_id)
            if not foods.exists():
                return Response(
                    {"detail": "No Foods Available."}, status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(foods, request)
            serializer = FoodReadSerializer(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, 7200)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(cached_data, request)
            serializer = FoodReadSerializer(paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, restaurant_id, format=None):
        # Create a new food
        serializer = FoodWriteSerializer(data=request.data)
        if serializer.is_valid():
            restaurant = get_object_or_404(Restaurant, id=restaurant_id)
            serializer.save(restaurant=restaurant)
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**food_detail_schema)
class FoodDetailView(APIView):
    """
    View to retrieve, update, and delete a food.

    Endpoints:
    - GET api/v1/restaurants/{id}/foods/{id}/
    - PUT api/v1/restaurants/{id}/foods/{id}/
    - DELETE api/v1/restaurants/{id}/foods/{id}/
    """

    permission_classes = [IsPartner]

    def get_object(self, food_id):
        # Get a food instance by id
        return get_object_or_404(Food, pk=food_id)

    def get(self, request, food_id, restaurant_id, format=None):
        # Get details of a food
        food = self.get_object(food_id)
        serializer = FoodReadSerializer(food)
        return Response(serializer.data)

    def put(self, request, food_id, format=None):
        # Update a food
        food = self.get_object(food_id)
        serializer = FoodWriteSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, food_id, format=None):
        # Delete a food
        food = self.get_object(food_id)
        food.is_available = False  # Logical deletion
        food.save()
        # Invalidate cache
        cache.delete("food")
        return Response(status=status.HTTP_204_NO_CONTENT)


class FoodDeletedListView(APIView):
    """
    View to list deleted foods.

    Endpoints:
    - GET api/v1/restaurants/{id}/foods/deleted/
    """

    permission_classes = [IsPartner]
    cache_key = "food_deleted_list"

    def get(self, request, format=None):
        # Get a list of deleted foods
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            foods = Food.objects.get_unavailable()
            if not foods.exists():
                return Response(
                    {"detail": "No Foods Available."}, status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(foods, request)
            serializer = FoodReadSerializer(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, 7200)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(cached_data, request)
            serializer = FoodReadSerializer(paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)
