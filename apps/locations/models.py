"""Models for Locations App."""

from django.db import models

from apps.utilities.models import BaseModel


class Region(BaseModel):
    """Model definition for Region (Entity)."""
    name = models.CharField(max_length=100, unique=True)
    number = models.PositiveSmallIntegerField(default=0)
    is_metropolitan = models.BooleanField(default=False)

    class Meta:
        ordering = ["pk"]
        verbose_name = "region"
        verbose_name_plural = "regions"

    def __str__(self):
        return str(self.name)


class Comune(BaseModel):
    """Model definition for Comune (Entity)."""
    name = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        ordering = ["pk"]
        verbose_name = "comune"
        verbose_name_plural = "comunes"
        indexes = [
            models.Index(fields=['region']),
        ]

    def __str__(self):
        return str(self.name)
