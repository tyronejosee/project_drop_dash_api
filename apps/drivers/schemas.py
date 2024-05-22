"""Schemas for Promotions App."""

from drf_spectacular.utils import extend_schema


driver_create_schema = {
    "post": extend_schema(
        operation_id="driver_list_create",
        summary="Create driver",
        description="pending",
    ),
}
