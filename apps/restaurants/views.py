"""Views for Restaurants App."""

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from .models import Restaurant
from .serializers import RestaurantSerializer
from .permissions import IsBusinessOwnerOrReadOnly
from apps.utilities.pagination import LargeSetPagination


class RestaurantListAPIView(APIView):
    """APIView to list and create restaurants."""
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """Get a list of restaurants."""
        stores = Restaurant.objects.filter(available=True).order_by("id")
        paginator = LargeSetPagination()
        page = paginator.paginate_queryset(stores, request)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": "No restaurants available."},
            status=status.HTTP_204_NO_CONTENT
        )

    def post(self, request):
        """Create a new restaurant."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetailAPIView(APIView):
    """APIView to retrieve, update, and delete a restaurant."""
    serializer_class = RestaurantSerializer
    permission_classes = [IsBusinessOwnerOrReadOnly]

    def get_object(self, restaurant_id):
        """Get a restaurant instance by id."""
        try:
            return Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, restaurant_id):
        """Get details of a restaurant."""
        store = self.get_object(restaurant_id)
        serializer = self.serializer_class(store)
        return Response(serializer.data)

    def put(self, request, restaurant_id):
        """Update a restaurant."""
        store = self.get_object(restaurant_id)
        serializer = self.serializer_class(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, restaurant_id):
        """Delete a restaurant."""
        store = self.get_object(restaurant_id)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
