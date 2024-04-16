"""Models for Menus App."""

from django.db import models

from apps.utilities.models import BaseModel
from apps.restaurants.models import Restaurant
from apps.foods.models import Food


class Menu(BaseModel):
    """Model definition for Menu (Pivot)."""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Menu."""
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return f"{self.restaurant}'s Menu - {self.food}"
