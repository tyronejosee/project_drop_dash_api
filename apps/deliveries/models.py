"""Models for Deliveries App."""

# from django.db import models
# from django.contrib.auth import get_user_model

# from apps.orders.models import Order
# from .choices import StatusChoices

# User = get_user_model()


# class Delivery(models.Model):
#     """Model definition for Delivery."""

#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     driver = models.ForeignKey(
#         User,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="deliveries",
#     )
#     delivery_date = models.DateTimeField()
#     pickup_address = models.CharField(max_length=255)
#     delivery_address = models.CharField(max_length=255)
#     contact_phone = models.CharField(max_length=15)
#     special_instructions = models.TextField(blank=True)
#     delivery_type = models.CharField(max_length=50)
#     delivery_cost = models.DecimalField(max_digits=10, decimal_places=2)
#     order_details = models.ForeignKey("Order", on_delete=models.CASCADE)
#     estimated_delivery_time = models.DateTimeField()
#     payment_status = models.BooleanField(default=False)
#     signature = models.ImageField(upload_to="deliveries/signatures/", blank=True)
#     internal_notes = models.TextField(blank=True)
#     status = models.CharField(
#         max_length=20, choices=StatusChoices.choices, default=StatusChoices.IN_PROGRESS
#     )
