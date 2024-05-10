"""Models for Utilities App."""

import uuid
from django.db import models


class BaseModel(models.Model):
    """Model definition for BaseModel (Base)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    available = models.BooleanField(default=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
