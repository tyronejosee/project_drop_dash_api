"""Filters for Reviews App."""

from django_filters import rest_framework as filters

from .models import Review


class ReviewFilter(filters.FilterSet):
    """Filter for Review model."""

    # ! TODO: Review and perform exhaustive testing

    rating = filters.NumberFilter(
        field_name="rating",
        label="Filter by exact rating, ex `/?rating=4`",
    )
    ordering = filters.OrderingFilter(
        fields=(
            ("rating", "best"),
            ("created_at", "newest"),
            ("created_at", "oldest"),
        ),
        field_labels={
            "rating": "Best",
            "created_at": "Newest",
            "-created_at": "Oldest",
        },
        label="Order by Best, Newest, Oldest, ex `/?ordering=best`",
    )

    class Meta:
        model = Review
        fields = [
            "rating",
            "ordering",
        ]
