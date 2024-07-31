"""Services for Orders App."""

from rest_framework import serializers


class OrderService:
    """
    Service class for handling Order related operations.
    """

    # ! TODO: Add tests

    @staticmethod
    def generate_transaction_field(order):
        """Generate the transaction ID based on Order IDs."""
        if not order.transaction:
            order.transaction = f"trans-{order.pk}"

    @staticmethod
    def validate_order(order):
        from .models import OrderItem

        if OrderItem.objects.filter(order_id=order.id).exists():
            order.is_valid = True
            order.save(update_fields=["is_valid"])


class OrderItemService:
    """
    Service class for handling OrderItem related operations.
    """

    @staticmethod
    def set_price(order_item):
        """Set the price based on the Food's sale price or regular price."""
        if order_item.food_id.sale_price:
            order_item.price = order_item.food_id.sale_price
        else:
            order_item.price = order_item.food_id.price
        return order_item

    @staticmethod
    def set_subtotal(order_item):
        """Set and calculate the subtotal for the OrderItem."""
        order_item.subtotal = order_item.price * order_item.quantity
        return order_item

    @staticmethod
    def validate_quantity(quantity):
        """Validate the quantity of an OrderItem."""
        if quantity > 10:
            raise serializers.ValidationError("Quantity cannot be greater than 10.")
        return quantity
