"""Models for Reviews App."""

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.utilities.models import BaseModel

User = settings.AUTH_USER_MODEL


class Review(BaseModel):
    """Model definition for Review."""

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)  # Test
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "review"
        verbose_name_plural = "reviews"
        unique_together = ["content_type", "object_id", "user"]

    def __str__(self):
        return str(f"{self.user} - {self.content_object}")
