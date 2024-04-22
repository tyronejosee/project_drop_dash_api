"""Views for Drivers App."""

from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from apps.utilities.pagination import LargeSetPagination
from .models import Driver
from .serializers import DriverSerializer


class DriverListAPIView(APIView):
    """API view to list and create drivers."""
    permission_classes = [IsAuthenticated]
    serializer_class = DriverSerializer
    cache_key = "fixed_coupon"
    cache_timeout = 7200  # 2 hours

    def get(self, request, format=None):
        # Get a list of drivers
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            drivers = Driver.objects.get_available()
            if not drivers.exists():
                return Response(
                    {"detail": "No drivers available"},
                    status=status.HTTP_204_NO_CONTENT
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(drivers, request)
            serializer = self.serializer_class(paginated_data, many=True)
            cache.set(self.cache_key, serializer.data, self.cache_timeout)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(
                cached_data, request)
            serializer = self.serializer_class(
                paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request, format=None):
        # Create a new driver
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DriverSerializer

    def get_object(self, driver_id):
        # Get a driver instance by id
        return get_object_or_404(Driver, pk=driver_id)

    def get(self, request, driver_id, format=None):
        driver = self.get_object(driver_id)
        serializer = self.serializer_class(driver)
        return Response(serializer.data)

    @transaction.atomic
    def put(self, request, driver_id, format=None):
        # Update a restaurant
        driver = self.get_object(driver_id)
        serializer = self.serializer_class(driver, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, driver_id, format=None):
        # Delete a restaurant
        driver = self.get_object(driver_id)
        driver.available = False  # Logical deletion
        driver.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
