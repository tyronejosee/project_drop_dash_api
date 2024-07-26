"""Models for Orders App."""

from django.db import models
from django.contrib.auth import get_user_model
from simple_history.models import HistoricalRecords

from apps.utilities.validators import validate_phone
from apps.utilities.models import BaseModel
from apps.restaurants.models import Restaurant
from apps.restaurants.models import Food
from apps.locations.models import Country, State, City
from apps.payments.choices import PaymentMethodChoices
from .services import OrderService, OrderItemService
from .managers import OrderManager, OrderItemManager
from .choices import OrderStatusChoices

User = get_user_model()


class Order(BaseModel):
    """Model definition for Order."""

    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shipping_name = models.CharField(max_length=255)
    shipping_phone = models.CharField(
        max_length=12,
        unique=True,
        validators=[validate_phone],
    )
    shipping_time = models.CharField(max_length=255)
    shipping_price = models.DecimalField(max_digits=5, decimal_places=2)
    transaction = models.CharField(max_length=255, unique=True, editable=False)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city_id = models.ForeignKey(City, on_delete=models.PROTECT)
    state_id = models.ForeignKey(State, on_delete=models.PROTECT)
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT)
    note = models.TextField(blank=True)
    zip_code = models.CharField(max_length=20)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
    )  # TODO: Add service method for subtotal orderitem
    status = models.CharField(
        max_length=50,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.NOT_PROCESSED,
    )
    payment_method = models.CharField(
        max_length=15,
        choices=PaymentMethodChoices.choices,
    )

    objects = OrderManager()
    history = HistoricalRecords()

    class Meta:
        ordering = ["pk"]
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return str(f"{self.shipping_name} - {self.transaction}")

    def save(self, *args, **kwargs):
        OrderService.set_transaction(self)
        super().save(*args, **kwargs)


class OrderItem(BaseModel):
    """Model definition for OrderItem."""

    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        editable=False,
    )
    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        editable=False,
        default=0,
    )

    objects = OrderItemManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "order item"
        verbose_name_plural = "order items"

    def __str__(self):
        return f"{self.order_id} - {self.food_id}"

    def save(self, *args, **kwargs):
        OrderItemService.set_price(self)
        OrderItemService.set_subtotal(self)
        super(OrderItem, self).save(*args, **kwargs)
