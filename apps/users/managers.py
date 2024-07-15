"""Managers for Users App."""

import re
from django.contrib.auth.models import BaseUserManager
from django.utils.text import slugify

from .choices import RoleChoices


class UserManager(BaseUserManager):
    """Manager for User instances."""

    def create_user(self, email, password=None, **kwargs):
        """Creates and returns a user with the given email and password."""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)

        def create_slug(username):
            # Normalize a username by removing special characters
            pattern = r'\badmin\b|[!@#$%^&*()_+-=[]{}|;:",.<>/?]|\s'

            if re.search(pattern, username):
                raise ValueError("Username contains invalid characters.")
            username = re.sub(pattern, "", username)
            return slugify(username)

        kwargs["slug"] = create_slug(kwargs["username"])
        user = self.model(email=email, **kwargs)
        kwargs.setdefault("role", RoleChoices.CLIENT)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        """Creates a superuser with the given email and password."""
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)
        kwargs.setdefault("role", RoleChoices.ADMINISTRATOR)

        if kwargs.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if kwargs.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        user = self.create_user(email, password=password, **kwargs)
        return user
