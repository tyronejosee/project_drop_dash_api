"""Schemas for Promotions App."""

from drf_spectacular.utils import extend_schema


food_list_schema = {
    "get": extend_schema(
        operation_id="food_list_retrieve",
        summary="Get foods",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="food_list_create",
        summary="Create food",
        description="pending",
    )
}


food_detail_schema = {
    "get": extend_schema(
        operation_id="food_detail_retrieve",
        summary="Get food",
        description="pending",
    ),
    "put": extend_schema(
        operation_id="food_detail_update",
        summary="Update food",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="food_detail_destroy",
        summary="Delete food",
        description="pending",
    )
}
