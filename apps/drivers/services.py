"""Services for Drivers App."""

import random
from decimal import Decimal
from django.conf import settings
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.functions import encrypt_field
from apps.users.choices import RoleChoices
from apps.deliveries.models import Delivery
from .choices import VehicleChoices, StatusChoices
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
        from apps.drivers.models import Driver

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
        if driver.is_verified:
            return Response(
                {"error": "The driver has already been verified."},
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
            {"error": "All required documents must be submitted for verification."},
            status=status.HTTP_403_FORBIDDEN,
        )

    @staticmethod
    def calculate_earnings(driver):
        """
        Calculate total earnings for a given driver.
        """
        # Add filter by day or date range
        deliveries = Delivery.objects.filter(driver_id=driver)
        total_earnings = sum(
            delivery.order_id.amount * Decimal(settings.DRIVER_TAX_RATE)
            for delivery in deliveries
        )

        # Add extra percentage based on the driver's status
        extra_percentage = Decimal(0)
        if driver.status == StatusChoices.BRONCE:
            extra_percentage = Decimal(0)  # 0%
        elif driver.status == StatusChoices.SILVER:
            extra_percentage = Decimal(0.25)  # 25%
        elif driver.status == StatusChoices.DIAMOND:
            extra_percentage = Decimal(0.50)  # 50%
        # If it is marked as ALERT, it loses all benefits

        total_earnings += total_earnings * extra_percentage
        return round(total_earnings, 2)  # Round to 2 decimal places

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

    @staticmethod
    def assign_driver_to_order(order):
        """
        Assign an available driver to a specific order.

        This method checks for available drivers who are verified and active,
        randomly selects one, and assigns them to the specified order.
        """
        from apps.drivers.models import Driver, DriverAssignment

        try:
            available_drivers = Driver.objects.get_available().filter(
                is_verified=True, is_active=True
            )
            # ! TODO: Add location filter

            # Check if there are available drivers
            if not available_drivers.exists():
                return {
                    "success": False,
                    "message": "No drivers available or active.",
                    "status_code": status.HTTP_404_NOT_FOUND,
                }

            # Randomly select a driver
            driver = random.choice(available_drivers)

            if DriverAssignment.objects.filter(order_id=order, driver_id=driver).exists():
                return {
                    "success": False,
                    "message": "The order has already been assigned.",
                    "status_code": status.HTTP_409_CONFLICT,
                }

            # Create the driver assignment
            DriverAssignment.objects.create(order_id=order, driver_id=driver)

            return {
                "success": True,
                "message": f"Driver {driver.id} assigned to order {order.id}.",
                "status_code": status.HTTP_200_OK,
            }
        except ObjectDoesNotExist:
            return {
                "success": False,
                "message": "Order or driver not found.",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        except Exception as e:
            return {
                "success": False,
                "message": str(e),
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            }
