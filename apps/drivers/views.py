"""Views for Drivers App."""

from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.utilities.functions import encrypt_field
from apps.users.permissions import IsClient, IsDriver
from apps.users.choices import Role
from .models import Driver, Resource
from .serializers import (
    DriverReadSerializer,
    DriverWriteSerializer,
    ResourceReadSerializer,
    ResourceWriteSerializer,
)
from .schemas import driver_create_schema


class DriverProfileView(APIView):
    """
    View to manage the driver profile.

    Endpoints:
    - GET api/v1/drivers/profile/
    - PATCH api/v1/drivers/profile/
    - DELETE api/v1/drivers/profile/
    """

    permission_classes = [IsDriver]

    def get_object(self, request):
        # Get a driver instance by user
        user = request.user
        return get_object_or_404(Driver, user=user)

    def get(self, request):
        # Get driver profile
        driver_profile = self.get_object(request)
        serializer = DriverReadSerializer(driver_profile)
        return Response(serializer.data)

    @transaction.atomic
    def patch(self, request):
        # Update driver profile
        driver_profile = self.get_object(request)

        if driver_profile.user == request.user:
            serializer = DriverReadSerializer(
                driver_profile, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"detail": "You are not the owner of this profile."},
            status=status.HTTP_403_FORBIDDEN,
        )

    @transaction.atomic
    def delete(self, request):
        # Delete driver profile
        driver_profile = self.get_object(request)
        if driver_profile.user == request.user:
            driver_profile.available = False  # Logical deletion
            # TODO: Add signal
            driver_profile.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {"detail": "You are not the owner of this profile."},
            status=status.HTTP_403_FORBIDDEN,
        )


@extend_schema_view(**driver_create_schema)
class DriverCreateView(APIView):
    """
    View to create a driver profile.

    Endpoints:
    - POST api/v1/drivers/
    """

    permission_classes = [IsClient()]

    @transaction.atomic
    def post(self, request):
        # Create a new driver
        # Check if the user already has a driver profile
        if Driver.objects.filter(user=request.user).exists():
            return Response(
                {"detail": "This user already has a driver profile."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = DriverWriteSerializer(data=request.data)
        if serializer.is_valid():

            # Encrypt specific fields after they have been validated
            validated_data = serializer.validated_data
            validated_data["phone"] = encrypt_field(validated_data["phone"])
            validated_data["address"] = encrypt_field(validated_data["address"])

            serializer.save(user=request.user)
            request.user.role = Role.DRIVER  # Update role
            request.user.save()
            cache.delete(self.cache_key)  # Invalidate cache
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverResourceRequestView(APIView):
    """
    View for requesting resources.

    Endpoints:
    - POST api/v1/resources/request/
    """

    permission_classes = [IsDriver]

    @transaction.atomic
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
