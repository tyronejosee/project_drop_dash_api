"""Services for Restaurants App."""

from decimal import Decimal
from django.conf import settings


class RestaurantService:
    """Service for Restaurant model."""

    pass


class FoodService:
    """Service for Food model."""

    @staticmethod
    def calculate_sale_price_with_tax(food):
        """Calculate the sale_price by adding the business-specific percentages."""
        base_price = Decimal(food.price)
        tax_amount = base_price * Decimal(settings.SALES_TAX_RATE)
        food.sale_price = base_price + tax_amount
