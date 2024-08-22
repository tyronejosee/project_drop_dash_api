"""Services for Orders App."""

from rest_framework import serializers
from rest_framework import status
from rest_framework.exceptions import ValidationError


class OrderService:
    """
    Service for Order model.
    """

    @staticmethod
    def generate_transaction_field(order):
        """Generate the transaction ID based on Order IDs."""
        if not order.transaction:
            order.transaction = f"trans-{order.pk}"

    @staticmethod
    def calculate_amount(order):
        """Calculate the total amount of the order based on quantity * price."""
        from .models import OrderItem

        order_items = OrderItem.objects.filter(order_id=order.id)
        total = sum(item.price * item.quantity for item in order_items)
        order.amount = total
        return order

    @staticmethod
    def validate_order(order):
        """Validate the order by checking if it has associated order items."""
        from .models import OrderItem

        if OrderItem.objects.filter(order_id=order.id).exists():
            order.is_valid = True
        else:
            order.is_valid = False

    @staticmethod
    def accept_order(order, driver):
        """Accept an order assignment and create a delivery entry."""
        from apps.drivers.models import DriverAssignment
        from apps.drivers.choices import AssignmentStatusChoices
        from apps.deliveries.models import Delivery
        from apps.deliveries.choices import StatusChoices

        try:
            # Find a pending assignment for the driver
            assignment = DriverAssignment.objects.filter(
                is_available=True,
                driver_id=driver,
                status=AssignmentStatusChoices.PENDING,
            ).first()

            if not assignment:
                return {
                    "success": False,
                    "message": "The order has already been accepted and assigned.",
                    "status_code": status.HTTP_409_CONFLICT,
                }

            # Update the assignment status
            assignment.status = AssignmentStatusChoices.ACCEPTED
            assignment.is_available = False
            assignment.save()

            # Create a delivery entry
            Delivery.objects.create(
                order_id=order,
                driver_id=driver,
                status=StatusChoices.ASSIGNED,
            )

            return {
                "success": True,
                "message": f"The order {order} was accepted.",
                "status_code": status.HTTP_200_OK,
            }
        except Exception as e:
            return {
                "success": False,
                "message": str(e),
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            }

    @staticmethod
    def reject_order(order, driver):
        """Reject an order assignment."""
        from apps.drivers.models import DriverAssignment
        from apps.drivers.choices import AssignmentStatusChoices

        try:
            assignment = DriverAssignment.objects.get(
                driver_id=driver,
                order_id=order,
            )

            # Checks if the assignment has already been rejected
            if assignment.status == AssignmentStatusChoices.REJECTED:
                return {
                    "success": False,
                    "message": "The order has already been rejected.",
                    "status_code": status.HTTP_409_CONFLICT,
                }

            assignment.status = AssignmentStatusChoices.REJECTED
            assignment.is_available = False
            assignment.save()

            return {
                "success": True,
                "message": f"The order {order} was rejected.",
                "status_code": status.HTTP_200_OK,
            }
        except DriverAssignment.DoesNotExist:
            return {
                "success": False,
                "message": "Assignment not found.",
                "status_code": status.HTTP_404_NOT_FOUND,
            }
        except Exception as e:
            return {
                "success": False,
                "message": str(e),
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
            }


class OrderItemService:
    """
    Service for OrderItem model.
    """

    @staticmethod
    def set_price(order_item):
        """Set the price based on the Food's sale price."""
        try:
            if order_item.food_id.sale_price:
                order_item.price = order_item.food_id.sale_price
            else:
                raise ValidationError(
                    {"detail": "Sale price are not defined for food item."},
                    code=status.HTTP_400_BAD_REQUEST,
                )
            return order_item
        except Exception as e:
            raise ValidationError(
                {"error": f"{e}"},
                code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    @staticmethod
    def validate_quantity(quantity):
        """Validate the quantity of an OrderItem."""
        if quantity > 10:
            raise serializers.ValidationError("Quantity cannot be greater than 10.")
        return quantity
