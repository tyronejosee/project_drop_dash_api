"""Models for Contents App."""

from django.db import models
from django.utils.text import slugify

from apps.utilities.models import BaseModel
from .choices import SPECIALTY_CHOICES


class Restaurant(BaseModel):
    """Model definition for Restaurant (Entity)."""
    name = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    image = models.ImageField(upload_to="restaurants/")
    description = models.TextField(blank=True)
    specialty = models.CharField(
        max_length=20, choices=SPECIALTY_CHOICES, default="varied")
    address = models.CharField(max_length=255)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    website = models.URLField(max_length=255, blank=True)
    is_open = models.BooleanField(default=False)

    class Meta:
        """Meta definition for Restaurant."""
        verbose_name = "Restaurant"
        verbose_name_plural = "Restaurants"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Override the save method to automatically generate the slug."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
