"""Paths for Utilities App."""

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
