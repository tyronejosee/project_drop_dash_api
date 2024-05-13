"""Models for Promotions App."""

from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator

from apps.utilities.validators import FileSizeValidator
from apps.utilities.models import BaseModel
from apps.utilities.paths import image_path
from .managers import PromotionManager

User = settings.AUTH_USER_MODEL


class Promotion(BaseModel):
    """Model definition for Promotion (Entity)."""
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    conditions = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to=image_path,
        validators=[
            FileExtensionValidator(allowed_extensions=["webp"]),
            FileSizeValidator(limit_mb=2)
        ]
    )

    objects = PromotionManager()

    class Meta:
        ordering = ["pk"]
        verbose_name = "promotion"
        verbose_name_plural = "promotions"

    def __str__(self):
        return str(self.name)
