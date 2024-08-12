"""Signals for Order App."""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import OrderItem


@receiver(post_save, sender=OrderItem)
def update_order_amount(sender, instance, created, **kwargs):
    """
    Signal to update the save method in Order model whenever an OrderItem is saved.
    """
    from .services import OrderService

    order = instance.order_id
    if created:
        OrderService.calculate_amount(order)
        order.save()
