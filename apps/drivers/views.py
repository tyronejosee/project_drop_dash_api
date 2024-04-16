"""Views for Drivers App."""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.utilities.pagination import LargeSetPagination
from .models import Driver
from .serializers import DriverSerializer


class DriverListAPIView(APIView):
    """API view to list and create drivers."""
    serializer_class = DriverSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        # Get a list of drivers
        drivers = Driver.objects.filter(available=True).order_by("id")
        if drivers.exists():
            paginator = LargeSetPagination()
            paginated_data = paginator.paginate_queryset(drivers, request)
            if paginated_data is not None:
                serializer = self.serializer_class(paginated_data, many=True)
                return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": "No drivers available"},
            status=status.HTTP_204_NO_CONTENT
        )

    def post(self, request, format=None):
        # Create a new driver
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DriverMeAPIView(APIView):
    """API view to retrieve the current user's driver information."""
    serializer_class = DriverSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        # Get the driver information for the current user
        user = request.user
        driver = Driver.objects.filter(user=user)  # .first()
        if driver.exists():
            serializer = self.serializer_class(driver)
            return Response(serializer.data)
        return Response(
            {"detail": "You do not have a registered driver account."},
            status=status.HTTP_404_NOT_FOUND
        )
