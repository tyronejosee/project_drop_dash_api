"""Services for Deliveries App."""

from django.utils import timezone
from rest_framework import status

from .models import Delivery, FailedDelivery
from .choices import StatusChoices


class DeliveryService:
    """
    Service for Delivery model.
    """

    @staticmethod
    def record_failed_delivery(order, driver, reason):
        """Register the failed delivery and update its status.."""
        FailedDelivery.objects.create(
            order_id=order,
            driver_id=driver,
            reason=reason,
            failed_at=timezone.now(),
        )

        # Update status
        delivery = Delivery.objects.get(order_id=order, driver_id=driver)
        delivery.status = StatusChoices.FAILED
        delivery.save()

    @staticmethod
    def mark_as_picked_up(order, driver):
        """Mark the delivery as picked up."""
        try:
            delivery = Delivery.objects.get(order_id=order, driver_id=driver)

            if delivery.status == StatusChoices.ASSIGNED:
                delivery.status = StatusChoices.PICKED_UP
                delivery.picked_up_at = timezone.now()
                delivery.save()

                return {
                    "success": True,
                    "message": "Delivery status was changed to 'Picked Up'.",
                    "status_code": status.HTTP_200_OK,
                }
            elif delivery.status == StatusChoices.PICKED_UP:
                return {
                    "success": False,
                    "message": "Delivery has already been marked as 'Picked Up'.",
                    "status_code": status.HTTP_409_CONFLICT,
                }
            else:
                return {
                    "success": False,
                    "message": "Delivery with status pending cannot be marked.",
                    "status_code": status.HTTP_400_BAD_REQUEST,
                }
        except Delivery.DoesNotExist:
            return {
                "success": False,
                "message": "Delivery not found.",
                "status_code": status.HTTP_404_NOT_FOUND,
            }

    @staticmethod
    def mark_as_delivered(order, driver, signature):
        """Mark the delivery status as completed."""
        try:
            delivery = Delivery.objects.get(order_id=order, driver_id=driver)

            if delivery.status == StatusChoices.PICKED_UP:
                # TODO: Add verification code
                delivery.signature = signature
                delivery.status = StatusChoices.DELIVERED
                delivery.delivered_at = timezone.now()
                delivery.is_completed = True
                delivery.save()

                return {
                    "success": True,
                    "message": "Order successfully delivered.",
                    "status_code": status.HTTP_200_OK,
                }
            else:
                return {
                    "success": False,
                    "message": "The status could not be changed, please try again.",
                    "status_code": status.HTTP_409_CONFLICT,
                }
        except Delivery.DoesNotExist:
            return {
                "success": False,
                "message": "Delivery not found.",
                "status_code": status.HTTP_400_BAD_REQUEST,
            }
