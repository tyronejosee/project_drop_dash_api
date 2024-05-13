"""Models for Orders App."""

from django.db import models
from django.contrib.auth import get_user_model

from apps.utilities.models import BaseModel
from apps.restaurants.models import Restaurant
from apps.restaurants.models import Food
from apps.locations.models import Comune, Region
from apps.payments.choices import PaymentMethod
from .managers import OrderManager, OrderItemManager
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

    objects = OrderManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return str(self.transaction)

    def save(self, *args, **kwargs):
        # Apply methods on save
        self.set_transaction()
        super().save(*args, **kwargs)

    def set_transaction(self):
        """Set the transaction ID based on Order IDs."""
        # if not self.transaction:
        self.transaction = f"trans-{self.pk}"


class OrderItem(BaseModel):
    """Model definition for OrderItem (Pivot)."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, editable=False)  # Ref
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True,
        editable=False, default=0)  # Ref
    # tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    objects = OrderItemManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "order item"
        verbose_name_plural = "order items"

    def __str__(self):
        return f"{self.order} - {self.food}"

    def save(self, *args, **kwargs):
        # Apply methods on save
        self.set_price()
        self.calculate_subtotal()
        super(OrderItem, self).save(*args, **kwargs)

    def set_price(self):
        """Set the price based on the Food's sale price or regular price."""
        if self.food.sale_price:
            self.price = self.food.sale_price
        else:
            self.price = self.food.price

    def calculate_subtotal(self):
        """Calculate the subtotal for the OrderItem."""
        self.subtotal = self.price * self.quantity
