"""Models for Orders App."""

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from simple_history.models import HistoricalRecords

from apps.utilities.validators import validate_phone
from apps.utilities.models import BaseModel
from apps.restaurants.models import Restaurant
from apps.restaurants.models import Food
from apps.locations.models import Country, State, City
from apps.payments.choices import PaymentMethodChoices
from .managers import OrderManager, OrderItemManager, OrderReportManager
from .choices import OrderStatusChoices, ReportStatusChoices

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
    transaction = models.CharField(max_length=255, unique=True, editable=False)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True)
    city_id = models.ForeignKey(City, on_delete=models.PROTECT)
    state_id = models.ForeignKey(State, on_delete=models.PROTECT)
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT)
    note = models.TextField(blank=True)
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        editable=False,
        default=0,
    )
    status = models.CharField(
        max_length=50,
        choices=OrderStatusChoices.choices,
        default=OrderStatusChoices.NOT_PROCESSED,
    )
    payment_method = models.CharField(
        max_length=15,
        choices=PaymentMethodChoices.choices,
    )
    is_payment = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)

    objects = OrderManager()
    history = HistoricalRecords()

    class Meta:
        ordering = ["pk"]
        verbose_name = "order"
        verbose_name_plural = "orders"
        indexes = [
            # Composite indexes
            models.Index(fields=["is_payment", "is_valid"]),
        ]

    def __str__(self):
        return str(f"{self.shipping_name} - {self.transaction}")

    def save(self, *args, **kwargs):
        from .services import OrderService

        OrderService.generate_transaction_field(self)
        OrderService.calculate_amount(self)
        OrderService.validate_order(self)
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
        help_text="The reference unit price of the product.",
    )

    objects = OrderItemManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "order item"
        verbose_name_plural = "order items"
        constraints = [
            models.UniqueConstraint(
                fields=["order_id", "food_id"], name="unique_order_food"
            )
        ]

    def __str__(self):
        return f"{self.order_id} - {self.food_id}"

    def save(self, *args, **kwargs):
        from .services import OrderItemService

        OrderItemService.set_price(self)
        super(OrderItem, self).save(*args, **kwargs)


class OrderRating(BaseModel):
    """Model definition for OrderRating."""

    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="order_ratings",
    )
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    comment = models.TextField(blank=True)

    class Meta:
        verbose_name = "order rating"
        verbose_name_plural = "order ratings"
        constraints = [
            models.UniqueConstraint(
                fields=["order_id", "user_id"],
                name="unique_order_user_rating",
            ),
        ]

    def __str__(self):
        return f"Rating {self.pk}"


class OrderReport(BaseModel):
    """Model definition for OrderReport."""

    order_id = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="order_reports",
    )
    reason = models.CharField(
        max_length=50,
        help_text="Short description of the reason for reporting",
    )
    description = models.TextField(
        blank=True,
        help_text="Detailed description of the issue",
    )
    status = models.CharField(
        max_length=20,
        choices=ReportStatusChoices.choices,
        default=ReportStatusChoices.PENDING,
    )
    is_resolved = models.BooleanField(default=False)

    objects = OrderReportManager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "order report"
        verbose_name_plural = "order reports"
        indexes = [
            models.Index(fields=["is_resolved"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["order_id", "user_id"],
                name="unique_order_user_report",
            ),
        ]

    def __str__(self):
        return f"Report {self.pk}"
