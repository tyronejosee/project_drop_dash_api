"""Paths for Utilities App."""

import os
from django.utils import timezone
from django.utils.text import slugify


def image_path(instance, filename):
    """Generates storage path for associated model images."""
    # appname = apps.contents.models
    appname = instance.__class__.__module__.split(".")[1]
    modelname = instance.__class__.__name__.lower()
    extension = filename.split(".")[-1]
    name_slug = slugify(instance.name)[:50]
    filename = f"{name_slug}.{extension}"

    return f"{appname}/{modelname}/{filename}"


def image_banner_path(instance, filename):
    """Generates storage path for associated model images."""
    # appname = apps.contents.models
    appname = instance.__class__.__module__.split(".")[1]
    modelname = instance.__class__.__name__.lower()
    extension = filename.split(".")[-1]
    name_slug = slugify(instance.name)[:50]
    filename = f"{name_slug}-banner.{extension}"

    return f"{appname}/{modelname}/{filename}"


def docs_path(instance, filename):
    """Generates storage path for associated model docs."""
    # appname = apps.contents.models
    appname = instance.__class__.__module__.split(".")[1]
    modelname = instance.__class__.__name__.lower()
    extension = filename.split(".")[-1]
    username = instance.user_id.username
    name_slug = slugify(instance.user_id.pk)[:50]
    filename = f"{name_slug}.{extension}"

    return f"{appname}/{modelname}/{username}/{filename}"


def signature_path(instance, filename):
    """Generate the upload path for the signature."""
    timestamp = timezone.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(
        "deliveries",
        "signatures",
        f"order_{instance.order_id.id}_driver_{instance.driver_id.id}_{timestamp}",
    )
