"""Models for Orders App."""

from django.db import models
from django.contrib.auth import get_user_model

from apps.utilities.validators import validate_phone
from apps.utilities.models import BaseModel
from apps.restaurants.models import Restaurant
from apps.restaurants.models import Food
from apps.locations.models import Country, State, City
from apps.payments.choices import PaymentMethod
from .managers import OrderManager, OrderItemManager
from .choices import OrderStatus

User = get_user_model()


class Order(BaseModel):
    """Model definition for Order (Entity)."""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shipping_name = models.CharField(max_length=255)
    shipping_phone = models.CharField(
        max_length=12, unique=True, validators=[validate_phone]
    )
    shipping_time = models.CharField(max_length=255)
    shipping_price = models.DecimalField(max_digits=5, decimal_places=2)
    transaction = models.CharField(max_length=255, unique=True, editable=False)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    note = models.TextField(blank=True)
    zip_code = models.CharField(max_length=20)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=50, choices=OrderStatus.choices, default=OrderStatus.NOT_PROCESSED
    )
    payment_method = models.CharField(
        max_length=15,
        choices=PaymentMethod.choices,
        default=PaymentMethod.BANK_TRANSFER,
    )

    objects = OrderManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return str(f"{self.shipping_name} - {self.transaction}")

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
    price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, editable=False
    )
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, editable=False, default=0
    )
    quantity = models.IntegerField()
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
