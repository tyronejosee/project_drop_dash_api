"""Views for Restaurants App."""

from django.db import transaction
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.pagination import LargeSetPagination
from apps.foods.models import Food
from apps.foods.serializers import FoodSerializer, FoodMiniSerializer
from apps.categories.models import Category
from .models import Restaurant
from .serializers import RestaurantSerializer
from .permissions import IsBusinessOwnerOrReadOnly


class RestaurantListAPIView(APIView):
    """APIView to list and create restaurants."""
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        # Get a list of restaurants
        stores = Restaurant.objects.filter(available=True).order_by("id")
        if stores.exists():
            paginator = LargeSetPagination()
            paginated_data = paginator.paginate_queryset(stores, request)
            serializer = self.serializer_class(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": "No restaurants available."},
            status=status.HTTP_404_NOT_FOUND
        )

    @transaction.atomic
    def post(self, request):
        # Create a new restaurant
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class RestaurantDetailAPIView(APIView):
    """APIView to retrieve, update, and delete a restaurant."""
    serializer_class = RestaurantSerializer
    permission_classes = [IsBusinessOwnerOrReadOnly]

    def get_object(self, restaurant_id):
        # Get a restaurant instance by id
        try:
            return Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, restaurant_id):
        # Get details of a restaurant
        store = self.get_object(restaurant_id)
        serializer = self.serializer_class(store)
        return Response(serializer.data)

    @transaction.atomic
    def put(self, request, restaurant_id):
        # Update a restaurant
        store = self.get_object(restaurant_id)
        serializer = self.serializer_class(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @transaction.atomic
    def delete(self, request, restaurant_id):
        # Delete a restaurant
        store = self.get_object(restaurant_id)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestaurantCategoriesAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, restaurant_id, formate=None):
        # Get a list of categories associated with a restaurant
        categories = Category.filter(restaurant=restaurant_id)
        if categories.exists():
            paginator = LargeSetPagination()
            paginated_data = paginator.paginate_queryset(categories, request)
            serializer = self.serializer_class(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": "No categories available."},
            status=status.HTTP_404_NOT_FOUND
        )


class RestaurantFoodsAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, restaurant_id, format=None):
        # Get a list of foods for a restaurant
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        foods = Food.objects.filter(restaurant=restaurant)
        if foods.exists():
            paginator = LargeSetPagination()
            paginated_data = paginator.paginate_queryset(foods, request)
            serializer = FoodMiniSerializer(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": "No foods available."},
            status=status.HTTP_404_NOT_FOUND
        )

    @transaction.atomic
    def post(self, request, restaurant_id, format=None):
        # Create a new food item for a restaurant
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(restaurant=restaurant)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class RestaurantFoodDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, restaurant_id, food_id, format=None):
        # Retrieve details for a food item associated with a restaurant
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        food = get_object_or_404(Food, id=food_id, restaurant=restaurant)
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def put(self, request, restaurant_id, food_id, format=None):
        # Update details for a food item associated with a restaurant
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        food = get_object_or_404(Food, id=food_id, restaurant=restaurant)
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, restaurant_id, food_id, format=None):
        # Delete a food item associated with a restaurant
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        food = get_object_or_404(Food, id=food_id, restaurant=restaurant)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# TODO: Add new permission
