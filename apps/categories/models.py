"""Models for Categories App."""

from django.db import models

from apps.utilities.models import BaseModel
from apps.restaurants.models import Restaurant
from .managers import CategoryManager


class Category(BaseModel):
    """Model definition for Category."""
    name = models.CharField(max_length=100)
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="categories"
    )

    objects = CategoryManager()

    class Meta:
        """Meta definition for Category."""
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)
