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
    """View to list and create orders."""
    permission_classes = [IsAuthenticated]
    cache_key = "order"
    cache_timeout = 7200  # 2 hours

    def get(self, request, format=None):
        # Get all available orders
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            orders = Order.objects.get_available()
            if not orders.exists():
                return Response(
                    {"detail": "No orders available."},
                    status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(orders, request)
            serializer = OrderSerializer(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, self.cache_timeout)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(
                cached_data, request)
            serializer = OrderSerializer(paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        # Create a new order
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(APIView):
    """View delete a order."""
    permission_classes = [IsAuthenticated]

    def get_object(self, order_id):
        # Get a order instance by id
        return get_object_or_404(Order, pk=order_id)

    def get(self, request, order_id, format=None):
        # Get details of a order
        order = self.get_object(order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def delete(self, request, order_id, format=None):
        # Delete a order
        order = self.get_object(order_id)
        order.available = False  # Logical deletion
        order.save()
        # Invalidate cache
        cache.delete("order")
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderItemListView(APIView):
    """View to list and create order items."""
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id, format=None):
        # Get all available items from an order
        order_items = OrderItem.objects.filter(order=order_id)
        if order_items.exists():
            serializer = OrderItemSerializer(order_items, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No order items available."},
            status=status.HTTP_404_NOT_FOUND
        )

    def post(self, request, order_id, format=None):
        # Create a item for an order
        request.data["order"] = order_id
        serializer = OrderItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderItemDetailView(APIView):
    """View to retrieve, update, or delete a specific order item."""
    permission_classes = [IsAuthenticated]

    def get(self, request, order_id, item_id, format=None):
        # Get the details of an item from an order
        order_item = OrderItem.objects.get(order=order_id, id=item_id)
        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data)

    def put(self, request, order_id, item_id, format=None):
        # Updates the details of an order item
        order_item = OrderItem.objects.get(order_id=order_id, id=item_id)
        serializer = OrderItemSerializer(order_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id, item_id, format=None):
        # Delete an item from an order
        order_item = OrderItem.objects.get(order_id=order_id, id=item_id)
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# TODO: Pending tests
