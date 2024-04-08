"""Models for Utilities App."""

import uuid
from django.db import models


class BaseModel(models.Model):
    """Model definition for BaseModel (Base)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    available = models.BooleanField(default=True, db_index=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
