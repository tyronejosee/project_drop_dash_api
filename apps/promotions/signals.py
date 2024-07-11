"""Signals for Promotions App."""

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

from .models import FixedCoupon, PercentageCoupon


@receiver(pre_save, sender=FixedCoupon)
@receiver(pre_save, sender=PercentageCoupon)
def update_coupon_status(sender, instance, **kwargs):
    """Signal update the status of coupon based on the end date and quantity."""
    if instance.end_date < timezone.now().date() or instance.quantity == 0:
        instance.is_active = False
        instance.is_available = False

        # TODO: Add Celery or Redis Queue
