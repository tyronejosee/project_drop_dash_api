"""Models for Finances App."""

from django.db import models

from apps.utilities.models import BaseModel
from .choices import TransactionTypeChoices


class Revenue(BaseModel):
    """Model definition for Revenue model."""

    order = models.ForeignKey(
        on_delete=models.DO_NOTHING,
        blank=True,
        related_name="revenues",
    )
    driver = models.ForeignKey(
        on_delete=models.DO_NOTHING,
        blank=True,
        related_name="revenues",
    )
    restaurant = models.ForeignKey(
        on_delete=models.DO_NOTHING,
        blank=True,
        related_name="revenues",
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(
        max_length=30,
        choices=TransactionTypeChoices.choices,
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = "Revenue"
        verbose_name_plural = "Revenues"
        indexes = [
            models.Index(fields=["order"]),
            models.Index(fields=["driver"]),
            models.Index(fields=["restaurant"]),
            models.Index(fields=["transaction_type"]),
        ]

    def __str__(self):
        return str(self.pk)
