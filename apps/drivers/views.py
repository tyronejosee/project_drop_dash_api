"""Views for Drivers App."""

from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsAdministrator, IsClient, IsDriver
from apps.utilities.pagination import LargeSetPagination
from apps.users.choices import Role
from .models import Driver, Resource
from .serializers import (
    DriverReadSerializer,
    DriverWriteSerializer,
    ResourceReadSerializer,
    ResourceWriteSerializer,
)
from .schemas import driver_list_schema, driver_detail_schema


@extend_schema_view(**driver_list_schema)
class DriverListView(APIView):
    """
    View to list and create drivers.

    Endpoints:
    - GET api/v1/drivers/
    - POST api/v1/drivers/
    """

    permission_classes = [IsAdministrator]
    serializer_class = DriverReadSerializer
    cache_key = "driver_list"
    cache_timeout = 7200  # 2 hours

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsClient()]
        return super().get_permissions()

    def get(self, request):
        # Get a list of drivers
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            drivers = Driver.objects.get_available()
            if not drivers.exists():
                return Response(
                    {"detail": "No drivers available"},
                    status=status.HTTP_204_NO_CONTENT,
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(drivers, request)
            serializer = self.serializer_class(paginated_data, many=True)
            cache.set(self.cache_key, serializer.data, self.cache_timeout)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(cached_data, request)
            serializer = self.serializer_class(paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request):
        # Create a new driver
        serializer = DriverWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            request.user.role = Role.DRIVER  # Update role
            request.user.save()
            cache.delete(self.cache_key)  # Invalidate cache
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**driver_detail_schema)
class DriverDetailView(APIView):
    """
    View to retrieve, update, and delete a driver.

    Endpoints:
    - GET api/v1/drivers/{id}/
    - PATCH api/v1/drivers/{id}/
    - DELETE api/v1/drivers/{id}/
    """

    permission_classes = [IsDriver]
    serializer_class = DriverReadSerializer

    def get_object(self, driver_id):
        # Get a driver instance by id
        return get_object_or_404(Driver, pk=driver_id)

    def get(self, request, driver_id, format=None):
        driver = self.get_object(driver_id)
        serializer = self.serializer_class(driver)
        return Response(serializer.data)

    @transaction.atomic
    def patch(self, request, driver_id):
        # Update a driver
        driver = self.get_object(driver_id)
        serializer = self.serializer_class(driver, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, driver_id):
        # Delete a driver
        driver = self.get_object(driver_id)
        driver.available = False  # Logical deletion
        driver.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DriverResourceRequestView(APIView):
    """
    View for requesting resources.

    Endpoints:
    - POST api/v1/resources/request/
    """

    permission_classes = [IsDriver]

    def post(self, request):
        # Submit a resource request
        serializer = ResourceWriteSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        driver = get_object_or_404(Driver, user=request.user)
        serializer.save(driver=driver)
        return Response(
            {"detail": "Request successful."}, status=status.HTTP_201_CREATED
        )


class DriverResourceHistoryView(APIView):
    """
    View for retrieving a driver's resource history.

    Endpoints:
    - GET api/v1/drivers/resources/history/
    """

    permission_classes = [IsDriver]

    def get(self, request, *args, **kwargs):
        # Retrieve a driver's resource history
        driver = get_object_or_404(Driver, user=request.user)
        resources = Resource.objects.filter(driver=driver)
        if not resources:
            return Response(
                {"detail": "There are no resources available."},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = ResourceReadSerializer(resources, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
