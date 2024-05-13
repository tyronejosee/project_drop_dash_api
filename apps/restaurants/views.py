"""Views for Restaurants App."""

from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsAdministrator, IsBusiness
from apps.utilities.pagination import LargeSetPagination
from .models import Restaurant, Category, Food
from .serializers import (
    RestaurantSerializer, CategorySerializer, CategoryListSerializer,
    FoodSerializer, FoodMiniSerializer)
from .schemas import (
    restaurant_list_schema, restaurant_detail_schema,
    restaurant_categories_schema, restaurant_foods_schema,
    category_list_schema, category_detail_schema,
    food_list_schema, food_detail_schema)


@extend_schema_view(**restaurant_list_schema)
class RestaurantListView(APIView):
    """APIView to list and create restaurants."""
    permission_classes = [IsAdministrator]
    serializer_class = RestaurantSerializer
    cache_key = "restaurant_list"

    def get(self, request):
        # Get a list of restaurants
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            restaurants = Restaurant.objects.get_available()
            if not restaurants.exists():
                return Response(
                    {"detail": "No restaurants available."},
                    status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(restaurants, request)
            # Set cache
            cache.set(self.cache_key, paginated_data, 7200)
            serializer = self.serializer_class(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)

        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(
                cached_data, request)
            serializer = self.serializer_class(
                paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request):
        # Create a new restaurant
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**restaurant_detail_schema)
class RestaurantDetailView(APIView):
    """APIView to retrieve, update, and delete a restaurant."""
    serializer_class = RestaurantSerializer
    permission_classes = [IsAdministrator]

    def get_object(self, restaurant_id):
        # Get a restaurant instance by id
        return get_object_or_404(Restaurant, pk=restaurant_id)

    def get(self, request, restaurant_id):
        # Get details of a restaurant
        restaurant = self.get_object(restaurant_id)
        serializer = self.serializer_class(restaurant)
        return Response(serializer.data)

    @transaction.atomic
    def put(self, request, restaurant_id):
        # Update a restaurant
        restaurant = self.get_object(restaurant_id)
        serializer = self.serializer_class(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, restaurant_id):
        # Delete a restaurant
        restaurant = self.get_object(restaurant_id)
        restaurant.available = False  # Logical deletion
        restaurant.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(**restaurant_categories_schema)
class RestaurantCategoriesView(APIView):
    permission_classes = [IsAdministrator]
    serializer_class = CategoryListSerializer

    def get(self, request, restaurant_id, format=None):
        # Get a list of categories associated with a restaurant
        categories = Category.objects.filter(restaurant=restaurant_id)
        if categories.exists():
            paginator = LargeSetPagination()
            paginated_data = paginator.paginate_queryset(categories, request)
            serializer = self.serializer_class(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": "No categories available."},
            status=status.HTTP_404_NOT_FOUND
        )


@extend_schema_view(**restaurant_foods_schema)
class RestaurantFoodsView(APIView):
    permission_classes = [IsAdministrator]
    serializer_class = FoodMiniSerializer

    def get(self, request, restaurant_id, format=None):
        # Get a list of foods for a restaurant
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        foods = Food.objects.get_foods_by_restaurant(restaurant)
        if foods.exists():
            paginator = LargeSetPagination()
            paginated_data = paginator.paginate_queryset(foods, request)
            serializer = self.serializer_class(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": "No foods available."},
            status=status.HTTP_404_NOT_FOUND
        )


@extend_schema_view(**category_list_schema)
class CategoryList(APIView):
    """APIView to list and create categories."""
    permission_classes = [IsAdministrator]
    serializer_class = CategorySerializer
    cache_key = "category_list"

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsBusiness()]
        return super().get_permissions()

    def get(self, request, format=None):
        # Get a list of categories
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            categories = Category.objects.get_all()
            # TODO: Fix query only restaurant
            if not categories.exists():
                return Response(
                    {"details": "No categories available."},
                    status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(categories, request)
            serializer = self.serializer_class(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, 7200)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(
                cached_data, request)
            serializer = self.serializer_class(
                paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        # Create a new category
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**category_detail_schema)
class CategoryDetailView(APIView):
    """APIView to retrieve, update, and delete a category."""
    permission_classes = [IsBusiness]
    serializer_class = CategorySerializer

    def get_object(self, category_id):
        # Get a category instance by id
        return get_object_or_404(Category, pk=category_id)

    def get(self, request, category_id):
        # Get details of a category
        category = self.get_object(category_id)
        serializer = self.serializer_class(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, category_id, format=None):
        # Update a category
        category = self.get_object(category_id)
        serializer = self.serializer_class(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        # Delete a category
        category = self.get_object(category_id)
        category.available = False  # Logical deletion
        category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(**food_list_schema)
class FoodListView(APIView):
    """APIView to list and create foods."""
    permission_classes = [IsBusiness]
    serializer_class = FoodSerializer
    cache_key = "food_list"

    def get(self, request, format=None):
        # Get a list of foods
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            foods = Food.objects.get_available()
            if not foods.exists():
                return Response(
                    {"detail": "No Foods Available."},
                    status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(foods, request)
            serializer = self.serializer_class(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, 7200)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(
                cached_data, request)
            serializer = self.serializer_class(
                paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        # Create a new food
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**food_detail_schema)
class FoodDetailView(APIView):
    """APIView to retrieve, update, and delete a food."""
    permission_classes = [IsBusiness]
    serializer_class = FoodSerializer

    def get_object(self, food_id):
        # Get a food instance by id
        return get_object_or_404(Food, pk=food_id)

    def get(self, request, food_id, format=None):
        # Get details of a food
        food = self.get_object(food_id)
        serializer = self.serializer_class(food)
        return Response(serializer.data)

    def put(self, request, food_id, format=None):
        # Update a food
        food = self.get_object(food_id)
        serializer = self.serializer_class(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, food_id, format=None):
        # Delete a food
        food = self.get_object(food_id)
        food.available = False  # Logical deletion
        food.save()
        # Invalidate cache
        cache.delete("food")
        return Response(status=status.HTTP_204_NO_CONTENT)


class FoodDeletedListView(APIView):
    """APIView to list deleted foods."""
    permission_classes = [IsBusiness]
    serializer_class = FoodSerializer
    cache_key = "food_deleted"
    cache_timeout = 7200  # 2 hours

    def get(self, request, format=None):
        # Get a list of deleted foods
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            foods = Food.objects.get_unavailable()
            if not foods.exists():
                return Response(
                    {"detail": "No Foods Available."},
                    status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(foods, request)
            serializer = self.serializer_class(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, self.cache_timeout)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(
                cached_data, request)
            serializer = self.serializer_class(
                paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)
