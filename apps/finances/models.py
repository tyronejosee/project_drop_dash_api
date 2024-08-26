"""Models for Finances App."""

from django.db import models

from apps.utilities.models import BaseModel
from apps.orders.models import Order
from apps.drivers.models import Driver
from apps.restaurants.models import Restaurant
from .managers import RevenueManager
from .choices import TransactionTypeChoices


class Revenue(BaseModel):
    """Model definition for Revenue model."""

    order_id = models.ForeignKey(
        Order,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    driver_id = models.ForeignKey(
        Driver,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    restaurant_id = models.ForeignKey(
        Restaurant,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=30,
        choices=TransactionTypeChoices.choices,
    )

    objects = RevenueManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "Revenue"
        verbose_name_plural = "Revenues"
        indexes = [
            models.Index(fields=["order_id"]),
            models.Index(fields=["driver_id"]),
            models.Index(fields=["restaurant_id"]),
            models.Index(fields=["transaction_type"]),
        ]

    def __str__(self):
        return str(self.pk)
