"""Services for Restaurants App."""

from decimal import Decimal
from django.conf import settings

from .models import Food


class RestaurantService:
    """
    Service for Restaurant model.
    """

    @staticmethod
    def update_restaurant_verification(restaurant):
        """
        Update the restaurant verification status based on the number of available foods.
        """
        # Count the number of foods for that restaurant
        food_count = Food.objects.filter(
            restaurant_id=restaurant, is_available=True
        ).count()

        # Mark the restaurant as is_verified if it has 5 or more available foods
        if food_count >= 5:
            restaurant.is_verified = True
            restaurant.save()


class FoodService:
    """
    Service for Food model.
    """

    @staticmethod
    def calculate_sale_price_with_tax(food):
        """Calculate the sale_price by adding the business-specific percentages."""
        base_price = Decimal(food.price)
        tax_amount = base_price * Decimal(settings.SALES_TAX_RATE)
        food.sale_price = base_price + tax_amount
