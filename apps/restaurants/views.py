"""Views for Restaurants App."""

from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.pagination import LargeSetPagination
from apps.foods.models import Food
from apps.foods.serializers import FoodMiniSerializer
from apps.categories.models import Category
from apps.categories.serializers import CategoryListSerializer
from .models import Restaurant
from .serializers import RestaurantSerializer
from .permissions import IsBusinessOrReadOnly


class RestaurantListView(APIView):
    """APIView to list and create restaurants."""
    permission_classes = [IsBusinessOrReadOnly]
    serializer_class = RestaurantSerializer
    cache_key = "restaurant"
    cache_timeout = 7200  # 2 hours

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
            cache.set(self.cache_key, paginated_data, self.cache_timeout)
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


class RestaurantDetailView(APIView):
    """APIView to retrieve, update, and delete a restaurant."""
    serializer_class = RestaurantSerializer
    permission_classes = [IsBusinessOrReadOnly]

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


class RestaurantCategoriesView(APIView):
    permission_classes = [IsBusinessOrReadOnly]
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


class RestaurantFoodsView(APIView):
    permission_classes = [IsBusinessOrReadOnly]
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
