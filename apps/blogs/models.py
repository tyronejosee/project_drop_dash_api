"""Models for Blogs App."""

from django.conf import settings
from django.db import models

from apps.utilities.models import BaseModel
from apps.utilities.mixins import SlugMixin
from .managers import TagManager, PostManager
from .choices import PriorityChoices, StatusChoices

User = settings.AUTH_USER_MODEL


class Tag(BaseModel, SlugMixin):
    """Model definition for Tag."""

    name = models.CharField(max_length=50, unique=True)

    objects = TagManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)


class Post(BaseModel, SlugMixin):
    """Model definition for Post."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.ManyToManyField(Tag)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
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
        self.set_slug()
        super().save(*args, **kwargs)


class PostReport(BaseModel):
    """Model definition for PostReport."""

    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    reason = models.TextField()
    priority = models.CharField(
        max_length=10,
        choices=PriorityChoices.choices,
        default=PriorityChoices.LOW,
    )
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING,
    )

    class Meta:
        ordering = ["pk"]
        verbose_name = "post report"
        verbose_name_plural = "post reports"

    def __str__(self):
        return str(f"{self.user} > {self.post}")
