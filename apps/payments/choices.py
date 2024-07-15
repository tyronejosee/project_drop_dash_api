"""Choices for Payments App."""

from django.db import models


class PaymentMethodChoices(models.TextChoices):

    CASH = "cash", "Cash"
    BANK_TRANSFER = "bank transfer", "Bank Transfer"
    CREDIT_CARD = "credit card", "Credit Card"
    DEBIT_CARD = "debit card", "Debit Card"
