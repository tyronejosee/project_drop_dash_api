"""Services for Finances App."""

from rest_framework import serializers

from .choices import TransactionTypeChoices


class RevenueService:
    """
    Service for Revenue model.
    """

    @staticmethod
    def validate_transaction_type(data):
        """
        Validates the `data` dictionary based on the `transaction_type` value.
        Ensures that certain fields are required depending on the `transaction_type`.
        """
        transaction_type = data.get("transaction_type")

        if (
            transaction_type == TransactionTypeChoices.DELIVERY_EARNINGS
            and not data.get("driver_id")
        ):
            raise serializers.ValidationError(
                {
                    "driver_id": "This field is required when the transaction type is 'Delivery Earnings'."
                }
            )

        if (
            transaction_type == TransactionTypeChoices.RESTAURANT_COMMISSION
            and not data.get("restaurant_id")
        ):
            raise serializers.ValidationError(
                {
                    "restaurant_id": "This field is required when the transaction type is 'Restaurant Commission'."
                }
            )

        # Add more validations...
        return data
