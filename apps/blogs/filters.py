"""Filters for Blogs App."""

from django_filters import rest_framework as filters

from apps.utilities.filters import BaseFilter
from .models import Post, Tag


class PostFilter(BaseFilter):
    """Filter for Post model."""

    tags = filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        label="Filter by tags, ex `/?tags=1,2,3`",
    )  # TODO: Fix field
    is_featured = filters.BooleanFilter(
        field_name="is_featured",
        label="Filter by featured status, ex `/?is_featured=true`",
    )

    class Meta:
        model = Post
        fields = [
            "tags",
            "is_featured",
        ]
