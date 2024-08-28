"""Models for Deliveries App."""

from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords

from apps.utilities.models import BaseModel
from apps.utilities.paths import signature_path
from apps.orders.models import Order
from apps.drivers.models import Driver
from .managers import DeliveryManager, FailedDeliveryManager
from .choices import StatusChoices

User = get_user_model()


class Delivery(BaseModel):
    """Model definition for Delivery."""

    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="deliveries",
    )
    signature = models.ImageField(
        upload_to=signature_path,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )
    picked_up_at = models.DateTimeField(blank=True, null=True)
    delivered_at = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    objects = DeliveryManager()
    history = HistoricalRecords()

    class Meta:
        ordering = ["pk"]
        verbose_name = "delivery"
        verbose_name_plural = "deliveries"
        indexes = [
            models.Index(fields=["order_id"]),
            models.Index(fields=["driver_id"]),
            models.Index(fields=["status"]),
            # Composite indexes
            models.Index(fields=["order_id", "status"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["order_id"],
                name="unique_order_delivery",
            ),
        ]

    def __str__(self):
        return f"Delivery for {self.order_id} - {self.status}"

    # ! TODO: Execute driver assignment logic within the save method


class FailedDelivery(BaseModel):
    """Model definition for FailedDelivery."""

    order_id = models.OneToOneField(Order, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    reason = models.CharField(max_length=255)
    failed_at = models.DateTimeField(blank=True, null=True)

    objects = FailedDeliveryManager()
    history = HistoricalRecords()

    class Meta:
        ordering = ["pk"]
        verbose_name = "failed delivery"
        verbose_name_plural = "failed deliveries"
        indexes = [
            models.Index(fields=["order_id"]),
            models.Index(fields=["driver_id"]),
        ]

    def __str__(self):
        return f"Failed Delivery: {self.order_id}"
