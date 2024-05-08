"""Schemas for Promotions App."""

from drf_spectacular.utils import extend_schema


driver_list_schema = {
    "get": extend_schema(
        operation_id="driver_list_retrieve",
        summary="Get drivers",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="driver_list_create",
        summary="Create driver",
        description="pending",
    )
}


driver_detail_schema = {
    "get": extend_schema(
        operation_id="driver_detail_retrieve",
        summary="Get driver",
        description="pending",
    ),
    "put": extend_schema(
        operation_id="driver_detail_update",
        summary="Update driver",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="driver_detail_destroy",
        summary="Delete driver",
        description="pending",
    )
}
