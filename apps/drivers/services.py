"""Services for Drivers App."""

from rest_framework.response import Response
from rest_framework import status

from apps.utilities.functions import encrypt_field
from apps.users.choices import RoleChoices
from .models import Driver
from .serializers import DriverWriteSerializer


class DriverService:
    """
    Service for Driver model.
    """

    @staticmethod
    def create_driver(user, data):
        """
        Create a new driver profile for the given user.

        This method checks if the user already has a driver profile. If not,
        it validates the provided data, encrypts sensitive fields (phone and address),
        saves the driver profile, and updates the user's role to DRIVER.
        """
        if Driver.objects.filter(user_id=user).exists():
            return Response(
                {"detail": "This user already has a driver profile."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = DriverWriteSerializer(data=data)
        if serializer.is_valid():
            # Encrypt specific fields after they have been validated
            validated_data = serializer.validated_data
            validated_data["phone"] = encrypt_field(validated_data["phone"])
            validated_data["address"] = encrypt_field(validated_data["address"])
            serializer.save(user_id=user)

            user.role = RoleChoices.DRIVER  # Update role
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def toggle_availability(driver):
        """
        Toggle the availability status of a driver.
        """
        driver.is_active = not driver.is_active
        driver.save()
        return driver.is_active
