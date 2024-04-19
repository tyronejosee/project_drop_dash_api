"""Models for Orders App."""

from django.db import models
from django.contrib.auth import get_user_model

from apps.utilities.models import BaseModel
from apps.restaurants.models import Restaurant
from apps.foods.models import Food
from apps.locations.models import Comune, Region
from apps.payments.choices import PaymentMethod
from .managers import OrderItemManager
from .choices import OrderStatus

User = get_user_model()


class Order(BaseModel):
    """Model definition for Order (Entity)."""
    transaction = models.CharField(max_length=255, unique=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    address = models.CharField(max_length=255)
    comune = models.ForeignKey(Comune, on_delete=models.PROTECT)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    phone = models.CharField(max_length=255)
    note = models.TextField(blank=True)
    status = models.CharField(
        max_length=50, choices=OrderStatus.choices,
        default=OrderStatus.NOT_PROCESSED)
    payment_method = models.CharField(
        max_length=15, choices=PaymentMethod.choices,
        default=PaymentMethod.CASH)

    class Meta:
        """Meta definition for Order model."""
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return str(self.transaction)

    def save(self, *args, **kwargs):
        # Generate transaction field
        if not self.transaction:
            self.transaction = f"{self.pk}/{self.user.pk}"
        super().save(*args, **kwargs)


class OrderItem(BaseModel):
    """Model definition for OrderItem (Pivot)."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Ref
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    count = models.IntegerField()

    objects = OrderItemManager()

    class Meta:
        """Meta definition for OrderItem model."""
        verbose_name = "order_item"
        verbose_name_plural = "order_items"

    def __str__(self):
        return f"{self.order} - {self.food}"
