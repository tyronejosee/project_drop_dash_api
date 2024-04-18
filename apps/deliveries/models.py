"""Models for Deliveries App."""


# class Delivery(models.Model):
#     DELIVERY_STATUS_CHOICES = [
#         ('IN_PROGRESS', 'In Progress'),
#         ('COMPLETED', 'Completed'),
#         ('CANCELLED', 'Cancelled')
#     ]
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
#     status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='IN_PROGRESS')
#     delivery_date = models.DateTimeField()


#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')
#     status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, default='IN_PROGRESS')
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

#     @classmethod
#     def create_from_order(cls, order):
#         if order.payment_status:
#             return cls.objects.create(order=order)
#         return None

# # Ejemplo de uso:
# # Crear una compra
# order = Order.objects.create(user=request.user, total_amount=100.00)

# # Realizar el pago
# order.payment_status = True
# order.save()

# # Activar la entrega
# delivery = Delivery.create_from_order(order)
# if delivery:
#     # La entrega se activó correctamente
#     pass
# else:
#     # El pago no se ha realizado
#     pass
