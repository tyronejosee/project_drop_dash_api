"""Models for Menus App."""

from django.conf import settings
from django.db import models

from apps.utilities.models import BaseModel
from apps.restaurants.models import Restaurant
from apps.foods.models import Food

User = settings.AUTH_USER_MODEL


class Menu(BaseModel):
    """Model definition for Menu (Entity)."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Menu."""
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return f"{self.user} {self.restaurant}"


class MenuItem(BaseModel):
    """Model definition for MenuItem (Pivot)."""
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Menu."""
        verbose_name = "MenuItem"
        verbose_name_plural = "MenuItems"

    def __str__(self):
        return self.menu
