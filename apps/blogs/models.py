"""Models for Blogs App."""

from django.conf import settings
from django.db import models
from django.utils.text import slugify

from apps.utilities.models import BaseModel
from .managers import PostManager

User = settings.AUTH_USER_MODEL


class Tag(BaseModel):
    """Model definition for Tag (Catalog)."""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ["pk"]
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # Override the save method to generate the slug
        if not self.slug or self.slug != self.name:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(BaseModel):
    """Model definition for Post (Entity)."""
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = PostManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        # Override the save method to generate the slug
        if not self.slug or self.slug != self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
