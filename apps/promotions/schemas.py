"""Schemas for Promotions App."""

from drf_spectacular.utils import extend_schema


promotion_list_schemas = {
    "get": extend_schema(
        operation_id="promotion_list_retrieve",
        summary="Get promotions",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="promotion_list_create",
        summary="Create promotion",
        description="pending",
    )
}


promotion_detail_schemas = {
    "get": extend_schema(
        operation_id="promotions_detail_retrieve",
        summary="Get promotion",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="promotions_detail_destroy",
        summary="Delete promotion",
        description="pending",
    )
}
