"""Models for Promotions App."""

# from django.db import models

# class Promotion(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name

# class PromotionCode(models.Model):
#     promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE, related_name='codes')
#     code = models.CharField(max_length=50, unique=True)
#     is_used = models.BooleanField(default=False)

#     def __str__(self):
#         return self.code


# def create_promotion(name, description, start_date, end_date):
#     promotion = Promotion.objects.create(
#         name=name,
#         description=description,
#         start_date=start_date,
#         end_date=end_date
#     )
#     return promotion


# def create_promotion_code(promotion):
#     code = generate_unique_code()  # Implementa lógica para generar un código único
#     promotion_code = PromotionCode.objects.create(
#         promotion=promotion,
#         code=code
#     )
#     return promotion_code


# def validate_promotion_code(code):
#     try:
#         promotion_code = PromotionCode.objects.get(code=code)
#         if promotion_code.is_used:
#             return False, "El código ya fue utilizado"
#         else:
#             promotion_code.is_used = True
#             promotion_code.save()
#             return True, "Código válido"
#     except PromotionCode.DoesNotExist:
#         return False, "Código inválido"
