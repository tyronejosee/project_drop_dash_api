"""Views for Orders App."""

from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsAdministrator, IsClient
from apps.utilities.pagination import LargeSetPagination
from .models import Order, OrderItem
from .serializers import (
    OrderWriteSerializer, OrderReadSerializer, OrderItemSerializer)
from .schemas import (
    order_list_schema, order_detail_schema,
    order_item_list_schema, order_item_detail_schema)


@extend_schema_view(**order_list_schema)
class OrderListView(APIView):
    """
    View to list and create orders.

    Endpoints:
    - GET api/v1/orders/
    - POST api/v1/orders/
    """
    permission_classes = [IsAdministrator]
    serializer_class = OrderWriteSerializer
    cache_key = "order"
    cache_timeout = 7200  # 2 hours

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsClient()]
        return super().get_permissions()

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
            serializer.save(user=request.user)
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**order_detail_schema)
class OrderDetailView(APIView):
    """
    View to retrieve and delete an order.

    Endpoints:
    - GET api/v1/orders/{id}/
    - DELETE api/v1/orders/{id}/
    """
    permission_classes = [IsClient]
    serializer_class = OrderReadSerializer

    def get_object(self, order_id):
        # Get a order instance by id
        return get_object_or_404(Order, pk=order_id)

    def get(self, request, order_id, format=None):
        # Get details of a order
        order = self.get_object(order_id)
        serializer = self.serializer_class(order)
        return Response(serializer.data)

    def delete(self, request, order_id, format=None):
        # Delete a order
        order = self.get_object(order_id)
        order.available = False  # Logical deletion
        order.save()
        cache.delete("order")  # Invalidate cache
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderMeView(APIView):
    """
    View of order profile for authenticated user (client).

    Endpoints:
    - GET api/v1/orders/me/
    """
    permission_classes = [IsClient]
    serializer_class = OrderReadSerializer

    def get(self, request, format=None):
        # Retrieve the order for the authenticated user
        order = Order.objects.get_by_user(request.user)
        if order.exists():
            serializer = self.serializer_class(order.first())
            return Response(serializer.data)
        return Response(
            {"detail": "You don't have a profile for orders created."},
            status=status.HTTP_404_NOT_FOUND
        )


@extend_schema_view(**order_item_list_schema)
class OrderItemListView(APIView):
    """
    View to list and create order items.

    Endpoints:
    - GET api/v1/orders/{id}/items/
    - POST api/v1/orders/{id}/items/
    """
    permission_classes = [IsClient]
    serializer_class = OrderItemSerializer

    def get(self, request, order_id, format=None):
        # Get all available items from an order
        order_items = OrderItem.objects.filter(order=order_id)
        if order_items.exists():
            serializer = self.serializer_class(order_items, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No order items available."},
            status=status.HTTP_404_NOT_FOUND
        )

    def post(self, request, order_id, format=None):
        # Create a item for an order
        request.data["order"] = order_id
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**order_item_detail_schema)
class OrderItemDetailView(APIView):
    """
    View to retrieve, update, or delete an order item.

    Endpoints:
    - GET api/v1/orders/{id}/items/{id}/
    - PATCH api/v1/orders/{id}/items/{id}/
    - DELETE api/v1/orders/{id}/items/{id}/
    """
    permission_classes = [IsClient]
    serializer_class = OrderItemSerializer

    def get(self, request, order_id, item_id, format=None):
        # Get the details of an item from an order
        order_item = OrderItem.objects.get(order=order_id, id=item_id)
        serializer = self.serializer_class(order_item)
        return Response(serializer.data)

    def patch(self, request, order_id, item_id, format=None):
        # Partial Update the details of an order item
        order_item = OrderItem.objects.get(order=order_id, id=item_id)
        serializer = self.serializer_class(
            order_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id, item_id, format=None):
        # Delete an item from an order
        order_item = OrderItem.objects.get(order_id=order_id, id=item_id)
        order_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
