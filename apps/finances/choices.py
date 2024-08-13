"""Choices for Finances App."""

from django.db import models


class TransactionTypeChoices(models.TextChoices):

    DELIVERY_EARNINGS = "delivery_earnings", "Delivery Earnings"
    RESTAURANT_COMMISSION = "restaurant_commission", "Restaurant Commission"
    DRIVER_WITHDRAWAL = "driver_withdrawal", "Driver Withdrawal"
    PROMOTIONAL_BONUS = "promotional_bonus", "Promotional Bonus"
    REFERRAL_BONUS = "referral_bonus", "Referral Bonus"
    OTHER_INCOME = "other_income", "Other Income"
    EXPENSE = "expense", "Expense"
    ADJUSTMENT = "adjustment", "Adjustment"
    MARKETING_EXPENSE = "marketing_expense", "Marketing Expense"
    OPERATIONAL_EXPENSE = "operational_expense", "Operational Expense"
    SUBSCRIPTION_REVENUE = "subscription_revenue", "Subscription Revenue"
    PARTNERSHIP_REVENUE = "partnership_revenue", "Partnership Revenue"
    REFUND = "refund", "Refund"
    TAXES = "taxes", "Taxes"
    LOAN_REPAYMENT = "loan_repayment", "Loan Repayment"
