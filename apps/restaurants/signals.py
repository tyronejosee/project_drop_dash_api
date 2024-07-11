"""Signals for Restaurants App."""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Food


@receiver(post_save, sender=Food)
def update_restaurant_verification(sender, instance, **kwargs):
    """Signal update the restaurant verification status."""
    restaurant = instance.restaurant

    # Count the number of foods for that restaurant
    product_count = Food.objects.filter(restaurant=restaurant, is_available=True).count()

    # Mark the restaurant as is_verified
    if product_count >= 5:
        restaurant.is_verified = True
        restaurant.save()
