"""Services for Orders App."""

from rest_framework import serializers


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


class OrderItemService:
    """
    Service for OrderItem model.
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
    def validate_quantity(quantity):
        """Validate the quantity of an OrderItem."""
        if quantity > 10:
            raise serializers.ValidationError("Quantity cannot be greater than 10.")
        return quantity
