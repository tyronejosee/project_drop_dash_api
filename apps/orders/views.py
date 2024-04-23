"""Views for Orders App."""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from apps.utilities.pagination import LargeSetPagination
from .models import Order
from .serializers import OrderSerializer


class OrderListView(APIView):
    """Pending."""
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        # Get all orders availables, order by id
        orders = Order.objects.filter(available=True).order_by("id")

        # Paginate all orders
        paginator = LargeSetPagination()
        paginated_data = paginator.paginate_queryset(orders, request)

        if paginated_data is not None:
            serializer = self.serializer_class(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)

        return Response(
            {"detail": "No orders available."},
            status=status.HTTP_204_NO_CONTENT
        )
