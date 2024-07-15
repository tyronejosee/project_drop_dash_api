"""Mixins for Utilities App."""

from django.db import models
from django.utils.text import slugify


class SlugMixin(models.Model):
    """Mixin providing slug functionality for models."""

    slug = models.SlugField(unique=True, blank=True)

    def set_slug(self):
        if hasattr(self, "name") and self.name:
            slug_name = slugify(self.name)[:50]
            if self.slug != slug_name:
                self.slug = slug_name
        elif hasattr(self, "title") and self.title:
            slug_title = slugify(self.title)[:50]
            if self.slug != slug_title:
                self.slug = slug_title

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     self.set_slug()
    #     super().save(*args, **kwargs)
