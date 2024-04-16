"""Models for Foods App."""

from django.db import models

from apps.utilities.models import BaseModel
from apps.restaurants.models import Restaurant
from apps.categories.models import Category


class Food(BaseModel):
    """Model definition for Food (Entity)."""
    name = models.CharField(max_length=255)
    description = models.TextField()
    normal_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to="foods/")
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="foods")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    is_vegetarian = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Food."""
        verbose_name = "Food"
        verbose_name_plural = "Foods"

    def __str__(self):
        return self.name
