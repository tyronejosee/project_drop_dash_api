"""Pagination for Utilities App."""

from rest_framework.pagination import PageNumberPagination


class SmallSetPagination(PageNumberPagination):
    """Pagination class for small sets of data."""
    page_query_param = "p"
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 5


class MediumSetPagination(PageNumberPagination):
    """Pagination class for medium sets of data."""
    page_query_param = "p"
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10


class LargeSetPagination(PageNumberPagination):
    """Pagination class for large sets of data."""
    page_query_param = "p"
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 25
