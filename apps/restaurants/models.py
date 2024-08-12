"""Models for Contents App."""

from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
from simple_history.models import HistoricalRecords

from apps.utilities.models import BaseModel
from apps.utilities.mixins import SlugMixin
from apps.utilities.paths import image_path, image_banner_path
from apps.utilities.validators import (
    FileSizeValidator,
    validate_phone,
    validate_food_image,
)
from apps.locations.models import Country, State, City
from .managers import RestaurantManager, CategoryManager, FoodManager
from .choices import SpecialtyChoices

User = settings.AUTH_USER_MODEL


class Restaurant(BaseModel, SlugMixin):
    """Model definition for Restaurant."""

    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, unique=True, db_index=True)
    image = models.ImageField(upload_to=image_path)
    banner = models.ImageField(upload_to=image_banner_path, blank=True)
    description = models.TextField(blank=True)
    specialty = models.CharField(
        max_length=20,
        choices=SpecialtyChoices.choices,
        default=SpecialtyChoices.VARIED,
    )
    address = models.CharField(max_length=255)
    city_id = models.ForeignKey(City, on_delete=models.PROTECT)
    state_id = models.ForeignKey(State, on_delete=models.PROTECT)
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    phone = models.CharField(max_length=12, unique=True, validators=[validate_phone])
    website = models.URLField(max_length=255, blank=True)
    is_open = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    banking_certificate = models.FileField(upload_to="documents/", blank=True)
    e_rut = models.FileField(upload_to="documents/", blank=True)
    legal_rep_email = models.EmailField(blank=True)
    legal_rep_identity_document = models.FileField(upload_to="documents/", blank=True)
    legal_rep_power_of_attorney = models.FileField(upload_to="documents/", blank=True)

    objects = RestaurantManager()
    history = HistoricalRecords()

    class Meta:
        ordering = ["pk"]
        verbose_name = "restaurant"
        verbose_name_plural = "restaurants"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)


class Category(BaseModel):
    """Model definition for Category."""

    name = models.CharField(max_length=100)
    restaurant_id = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="categories",
    )

    objects = CategoryManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.name)


class Food(BaseModel):
    """Model definition for Food (Entity)."""

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="base price of the product, excluding taxes and surcharges.",
    )
    sale_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
        blank=True,
        editable=False,
        help_text="Total price plus taxes.",
    )
    image = models.ImageField(
        upload_to=image_path,
        validators=[
            FileExtensionValidator(allowed_extensions=["webp"]),
            FileSizeValidator(limit_mb=1),
            validate_food_image,
        ],
    )
    restaurant_id = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="foods",
    )
    category_id = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
    )
    is_vegetarian = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    objects = FoodManager()
    history = HistoricalRecords()

    class Meta:
        ordering = ["pk"]
        verbose_name = "food"
        verbose_name_plural = "foods"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        from .services import FoodService

        FoodService.calculate_sale_price_with_tax(self)
        super().save(*args, **kwargs)
