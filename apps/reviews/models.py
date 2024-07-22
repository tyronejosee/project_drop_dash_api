"""Models for Reviews App."""

from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

from apps.utilities.models import BaseModel

User = settings.AUTH_USER_MODEL


class Review(BaseModel):
    """Model definition for Review."""

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={"model__in": ["restaurant", "post"]},
    )
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "review"
        verbose_name_plural = "reviews"
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=["content_type", "object_id", "user_id"],
                name="unique_reviews_user",
            )
        ]

    def __str__(self):
        return str(f"{self.user_id} - {self.content_object}")

    def save(self, *args, **kwargs):
        if self.content_type.model not in ["restaurant", "post"]:
            raise ValidationError("Invalid model relationship")
        super(Review, self).save(*args, **kwargs)
