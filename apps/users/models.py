"""Models for Users App."""

import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords

from .managers import UserManager
from .choices import RoleChoices


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User (Entity)."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    username = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    date_birth = models.DateField(null=True, blank=True)
    points = models.IntegerField(default=0)
    role = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.CLIENT,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    history = HistoricalRecords()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ["pk"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return str(self.username)

    @property
    def full_name(self):
        """Return the user's full name."""
        return f"{self.first_name} {self.last_name}"
