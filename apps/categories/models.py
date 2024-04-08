"""Models for Categories App."""

from django.db import models
from django.utils.text import slugify

from apps.utilities.models import BaseModel


class Category(BaseModel):
    """Model definition for Category."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        """Meta definition for Category."""
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

    def save(self, *args, **kwargs):
        """Override the save method to automatically generate the slug."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
