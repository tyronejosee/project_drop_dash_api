"""Services for Drivers App."""

from django.core.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.functions import encrypt_field
from apps.users.choices import RoleChoices
from .choices import VehicleChoices
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
        from .models import Driver

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
    def verify_driver(driver):
        """
        Verifies the driver if all required documents have been submitted.
        """
        # TODO: Consider the possibility of separating the HTTP responses further
        if driver.is_verified:
            return Response(
                {"detail": "The driver has already been verified."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if all(
            [
                driver.driver_license,
                driver.identification_document,
                driver.social_security_certificate,
                driver.criminal_record_certificate,
            ]
        ):
            driver.is_verified = True
            driver.save()
            return Response(
                {"detail": "Driver verified successfully."},
                status=status.HTTP_200_OK,
            )
        return Response(
            {"detail": "All required documents must be submitted for verification."},
            status=status.HTTP_403_FORBIDDEN,
        )

    @staticmethod
    def toggle_availability(driver):
        """
        Toggle the availability status of a driver.
        """
        driver.is_active = not driver.is_active
        driver.save()
        return driver.is_active

    @staticmethod
    def validate_driver_license(driver):
        """
        Validates the presence of a driver license based on the vehicle type.

        If the vehicle type is not 'bicycle', 'driver license' is required.
        """
        if driver.vehicle_type != VehicleChoices.BICYCLE and not driver.driver_license:
            raise ValidationError(
                {
                    "driver_license": "Driver license is required for automobiles and motorcycles."
                }
            )
