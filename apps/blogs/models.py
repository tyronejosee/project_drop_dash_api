"""Models for Blogs App."""

from django.conf import settings
from django.db import models
from django.utils.text import slugify

from apps.utilities.models import BaseModel
from .managers import TagManager, PostManager
from .choices import Priority, Status

User = settings.AUTH_USER_MODEL


class Tag(BaseModel):
    """Model definition for Tag (Catalog)."""

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    objects = TagManager()

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
    points = models.IntegerField(default=100)
    is_featured = models.BooleanField(default=False)

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


class PostReport(BaseModel):
    """Model definition for PostReport (Pivot)."""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.TextField()
    priority = models.CharField(
        max_length=10, choices=Priority.choices, default=Priority.LOW
    )
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PENDING
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = "post report"
        verbose_name_plural = "post reports"

    def __str__(self):
        return str(f"{self.user} > {self.post}")
