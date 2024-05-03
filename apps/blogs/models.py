"""Models for Blogs App."""

from django.conf import settings
from django.db import models
from django.utils.text import slugify

from apps.utilities.models import BaseModel

User = settings.AUTH_USER_MODEL


class Tag(BaseModel):
    """Model definition for Tag (Catalog)."""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        """Meta definition for Post."""
        ordering = ["pk"]
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        """Override the save method to automatically generate the slug."""
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(BaseModel):
    """Model definition for Post (Entity)."""
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Post."""
        ordering = ["pk"]
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        """Override the save method to automatically generate the slug."""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
