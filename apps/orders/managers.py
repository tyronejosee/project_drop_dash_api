"""Managers for Orders App."""

from django.db import models

from .choices import OrderStatus


class OrderManager(models.Manager):
    """Manager for Order Model."""

    def get_queryset(self):
        return super().get_queryset().filter(available=True)

    def not_processed_orders(self):
        return self.get_queryset().filter(status=OrderStatus.NOT_PROCESSED)

    def processed_orders(self):
        return self.get_queryset().filter(status=OrderStatus.PROCESSED)

    def shipping_orders(self):
        return self.get_queryset().filter(status=OrderStatus.SHIPPING)

    def delivered_orders(self):
        return self.get_queryset().filter(status=OrderStatus.DELIVERED)

    def cancelled_orders(self):
        return self.get_queryset().filter(status=OrderStatus.CANCELLED)


class OrderItemManager(models.Manager):
    """Manager for OrderItem Model."""

    def get_queryset(self):
        return super().get_queryset().filter(available=True)

    def calculate_total_price_and_tax(self, order_item):
        price = order_item.price
        discount = order_item.discount
        tax_percentage = order_item.tax_percentage
        count = order_item.count

        tax = (price * tax_percentage / 100) * count
        total_price = (price * count) - discount + tax
        return total_price, tax
