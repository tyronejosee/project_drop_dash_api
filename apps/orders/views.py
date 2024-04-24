"""Views for Orders App."""

from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.utilities.pagination import LargeSetPagination
from .models import Order, OrderItem
from .serializers import OrderSerializer, OrderItemSerializer


class OrderListView(APIView):
    """APIView to list and create orders."""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    cache_key = "order"
    cache_timeout = 7200  # 2 hours

    def get(self, request, format=None):
        # Get all available orders
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            orders = Order.objects.filter(available=True)
            if not orders.exists():
                return Response(
                    {"detail": "No orders available."},
                    status=status.HTTP_204_NO_CONTENT
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(orders, request)
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
        # Create a new order
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    """APIView delete a order."""
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_object(self, order_id):
        # Get a order instance by id
        return get_object_or_404(Order, pk=order_id)

    def delete(self, request, order_id, format=None):
        # Delete a food
        order = self.get_object(order_id)
        order.available = False  # Logical deletion
        order.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemListView(APIView):
    """APIView delete a order."""

    def get(self, request, order_id, format=None):
        order_items = OrderItem.objects.filter(order=order_id)

        if order_items.exists():
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "There are no items available for this order."},
            status=status.HTTP_404_NOT_FOUND
        )
