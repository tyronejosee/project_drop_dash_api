"""Schemas for Orders App."""

from drf_spectacular.utils import extend_schema


order_list_schema = {
    "get": extend_schema(
        operation_id="order_list_retrieve",
        summary="Get orders",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="order_list_create",
        summary="Create order",
        description="pending",
    )
}


order_detail_schema = {
    "get": extend_schema(
        operation_id="order_detail_retrieve",
        summary="Get order",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="order_detail_destroy",
        summary="Delete order",
        description="pending",
    )
}


order_item_list_schema = {
    "get": extend_schema(
        operation_id="order_item_list_retrieve",
        summary="Get orders",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="order_item_list_create",
        summary="Create order",
        description="pending",
    )
}


order_item_detail_schema = {
    "get": extend_schema(
        operation_id="order_item_detail_retrieve",
        summary="Get order item",
        description="pending",
    ),
    "put": extend_schema(
        operation_id="order_item_detail_update",
        summary="Update order item",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="order_item_detail_destroy",
        summary="Delete order item",
        description="pending",
    )
}
