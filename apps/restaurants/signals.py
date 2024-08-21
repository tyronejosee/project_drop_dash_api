"""Signals for Restaurants App."""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Food
from .services import RestaurantService


@receiver(post_save, sender=Food)
def handle_food_post_save(sender, instance, **kwargs):
    """Signal update the restaurant verification status."""
    restaurant = instance.restaurant_id
    RestaurantService.update_restaurant_verification(restaurant)
