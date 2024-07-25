"""Pagination for Utilities App."""

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination


class LimitSetPagination(LimitOffsetPagination):
    """Pagination for datasets with limit and offset."""

    default_limit = 25
    limit_query_description = "Number of results to return per page, ex `/?limit=50`"
    limit_query_param = "limit"
    max_limit = 50
    offset_query_description = (
        "The initial index from which to return the results, ex `/?ffset=20`"
    )
    offset_query_param = "offset"
    template = "rest_framework/pagination/numbers.html"


class SmallSetPagination(PageNumberPagination):
    """Paginator for small sets of data."""

    page_query_param = "p"
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 5


class MediumSetPagination(PageNumberPagination):
    """Paginator for medium sets of data."""

    page_query_param = "p"
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10


class LargeSetPagination(PageNumberPagination):
    """Paginator for large sets of data."""

    page_query_param = "p"
    page_size = 25
    page_size_query_param = "page_size"
    max_page_size = 25
