"""Schemas for Promotions App."""

from drf_spectacular.utils import extend_schema


category_list_schema = {
    "get": extend_schema(
        operation_id="category_list_retrieve",
        summary="Get categories",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="category_list_create",
        summary="Create category",
        description="pending",
    )
}


category_detail_schema = {
    "get": extend_schema(
        operation_id="category_detail_retrieve",
        summary="Get category",
        description="pending",
    ),
    "put": extend_schema(
        operation_id="category_detail_update",
        summary="Update category",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="category_detail_destroy",
        summary="Delete category",
        description="pending",
    )
}
