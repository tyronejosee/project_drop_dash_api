"""Views for Foods App."""

from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.utilities.pagination import LargeSetPagination
from apps.restaurants.permissions import IsBusinessOrReadOnly
from .models import Food
from .serializers import FoodSerializer
from .schemas import food_list_schema, food_detail_schema


@extend_schema_view(**food_list_schema)
class FoodListView(APIView):
    """APIView to list and create foods."""
    permission_classes = [IsBusinessOrReadOnly]
    serializer_class = FoodSerializer
    cache_key = "food"
    cache_timeout = 7200  # 2 hours

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
            cache.set(self.cache_key, serializer.data, self.cache_timeout)
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
    permission_classes = [IsBusinessOrReadOnly]
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
    permission_classes = [IsBusinessOrReadOnly]
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
