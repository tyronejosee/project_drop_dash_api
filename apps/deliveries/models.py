"""Models for Deliveries App."""

from django.db import models
from simple_history.models import HistoricalRecords

from apps.utilities.models import BaseModel
from apps.utilities.paths import signature_path
from apps.orders.models import Order
from apps.drivers.models import Driver
from .managers import DeliveryManager
from .choices import StatusChoices


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
    picked_up_at = models.DateTimeField(blank=True)
    delivered_at = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)

    objects = DeliveryManager()
    history = HistoricalRecords()

    class Meta:
        ordering = ["pk"]
        verbose_name = "delivery"
        verbose_name_plural = "deliveries"
        indexes = [
            models.Index(fields=["order"]),
            models.Index(fields=["driver"]),
            models.Index(fields=["status"]),
            # Composite indexes
            models.Index(fields=["order", "status"]),
        ]
        constraints = [
            models.UniqueConstraint(fields=["order"], name="unique_order_delivery"),
        ]

    def __str__(self):
        return f"Delivery for Order {self.order.id} - {self.status}"

    def save(self, *args, **kwargs):
        if self.status == StatusChoices.DELIVERED:
            self.is_completed = True
        super().save(*args, **kwargs)
