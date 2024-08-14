# """Views for Restaurants App."""

# import re
# from django.db import transaction
# from django.contrib.contenttypes.models import ContentType
# from django.core.cache import cache
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.permissions import AllowAny
# from drf_spectacular.utils import extend_schema_view

# from apps.orders.models import Order
# from apps.orders.serializers import OrderReadSerializer
# from apps.reviews.models import Review
# from apps.reviews.serializers import ReviewReadSerializer, ReviewWriteSerializer
# from apps.users.permissions import IsPartner, IsClient
# from apps.utilities.pagination import LargeSetPagination
# from .models import Restaurant, Category, Food
# from .serializers import (
#     RestaurantReadSerializer,
#     RestaurantWriteSerializer,
#     CategoryReadSerializer,
#     CategoryWriteSerializer,
#     FoodReadSerializer,
#     FoodWriteSerializer,
# )


# @extend_schema_view(**food_list_schema)
# class FoodListView(APIView):
#     """
#     View to list and create foods.

#     Endpoints:
#     - GET api/v1/restaurants/{id}/foods/
#     - POST api/v1/restaurants/{id}/foods/
#     """

#     permission_classes = [AllowAny]
#     cache_key = "food_list"

#     def get_permissions(self):
#         if self.request.method == "POST":
#             return [IsPartner()]
#         return super().get_permissions()

#     def get(self, request, restaurant_id, format=None):
#         # Get a list of foods
#         paginator = LargeSetPagination()
#         cached_data = cache.get(self.cache_key)

#         if cached_data is None:
#             foods = Food.objects.get_foods_by_restaurant(restaurant_id)
#             if not foods.exists():
#                 return Response(
#                     {"detail": "No Foods Available."}, status=status.HTTP_404_NOT_FOUND
#                 )
#             # Fetches the data from the database and serializes it
#             paginated_data = paginator.paginate_queryset(foods, request)
#             serializer = FoodReadSerializer(paginated_data, many=True)
#             # Set cache
#             cache.set(self.cache_key, serializer.data, 7200)
#         else:
#             # Retrieve the cached data and serialize it
#             paginated_cached_data = paginator.paginate_queryset(cached_data, request)
#             serializer = FoodReadSerializer(paginated_cached_data, many=True)

#         return paginator.get_paginated_response(serializer.data)

#     def post(self, request, restaurant_id, format=None):
#         # Create a new food
#         serializer = FoodWriteSerializer(data=request.data)
#         if serializer.is_valid():
#             restaurant = get_object_or_404(
#                 Restaurant, id=restaurant_id
#             )  # ! TODO: Fix variable and field name
#             serializer.save(restaurant_id=restaurant)
#             # Invalidate cache
#             cache.delete(self.cache_key)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @extend_schema_view(**food_detail_schema)
# class FoodDetailView(APIView):
#     """
#     View to retrieve, update, and delete a food.

#     Endpoints:
#     - GET api/v1/restaurants/{id}/foods/{id}/
#     - PUT api/v1/restaurants/{id}/foods/{id}/
#     - DELETE api/v1/restaurants/{id}/foods/{id}/
#     """

#     permission_classes = [IsPartner]

#     def get_object(self, food_id):
#         # Get a food instance by id
#         return get_object_or_404(Food, pk=food_id)

#     def get(self, request, food_id, restaurant_id, format=None):
#         # Get details of a food
#         food = self.get_object(food_id)
#         serializer = FoodReadSerializer(food)
#         return Response(serializer.data)

#     def put(self, request, food_id, format=None):
#         # Update a food
#         food = self.get_object(food_id)
#         serializer = FoodWriteSerializer(food, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, food_id, format=None):
#         # Delete a food
#         food = self.get_object(food_id)
#         food.is_available = False  # Logical deletion
#         food.save()
#         # Invalidate cache
#         cache.delete("food")
#         return Response(status=status.HTTP_204_NO_CONTENT)
