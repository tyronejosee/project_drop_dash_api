"""Mixins for Utilities App."""

from django.db import models
from django.http import Http404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.utils.text import slugify

from rest_framework.response import Response
from rest_framework import status


class SlugMixin(models.Model):
    """Mixin providing slug functionality for models."""

    slug = models.SlugField(unique=True, blank=True)

    def set_slug(self):
        if hasattr(self, "name") and self.name:
            slug_name = slugify(self.name)[:50]
            if self.slug != slug_name:
                self.slug = slug_name
        elif hasattr(self, "title") and self.title:
            slug_title = slugify(self.title)[:50]
            if self.slug != slug_title:
                self.slug = slug_title
        elif hasattr(self, "word") and self.word:
            slug_word = slugify(self.word)[:50]
            if self.slug != slug_word:
                self.slug = slug_word

    class Meta:
        abstract = True


class ListCacheMixin:
    """Mixin provides caching for the list methods of viewsets."""

    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class LogicalDeleteMixin:
    """Mixin for logical deletion of instances."""

    def destroy(self, request, *args, **kwargs):
        """Deletes the instance logically by marking it as unavailable."""
        try:
            instance = self.get_object()
            instance.is_available = False
            instance.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Http404:
            return Response(
                {"detail": "Resource not found."}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ReadOnlyFieldsMixin:
    """Mixin to make all serializer fields read-only."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].read_only = True
