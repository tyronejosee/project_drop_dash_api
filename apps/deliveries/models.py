"""Models for Deliveries App."""

# from django.db import models


# class Delivery(models.Model):
#     DELIVERY_STATUS_CHOICES = [
#         ('IN_PROGRESS', 'In Progress'),
#         ('COMPLETED', 'Completed'),
#         ('CANCELLED', 'Cancelled')
#     ]
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     driver = models.ForeignKey(
#         User, on_delete=models.SET_NULL, null=True,
#         blank=True, related_name='deliveries')
#     status = models.CharField(
#         max_length=20, choices=DELIVERY_STATUS_CHOICES,
#         default='IN_PROGRESS')
#     delivery_date = models.DateTimeField()

#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     driver = models.ForeignKey(
#         User, on_delete=models.SET_NULL,
#         null=True, blank=True, related_name='deliveries')
#     status = models.CharField(
#         max_length=20, choices=DELIVERY_STATUS_CHOICES,
#         default='IN_PROGRESS')
#     delivery_date = models.DateTimeField()
#     pickup_address = models.CharField(max_length=255)
#     delivery_address = models.CharField(max_length=255)
#     contact_phone = models.CharField(max_length=15)
#     special_instructions = models.TextField(blank=True)
#     delivery_type = models.CharField(max_length=50)
#     delivery_cost = models.DecimalField(max_digits=10, decimal_places=2)
#     order_details = models.ForeignKey('Order', on_delete=models.CASCADE)
#     estimated_delivery_time = models.DateTimeField()
#     payment_status = models.BooleanField(default=False)
#     signature = models.ImageField(upload_to='signatures/', blank=True)
#     internal_notes = models.TextField(blank=True)
