"""Schemas for Promotions App."""

from drf_spectacular.utils import extend_schema


fixed_coupon_list_schema = {
    "get": extend_schema(
        operation_id="fixed_coupon_list_retrieve",
        summary="Get fixed coupons",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="fixed_coupon_list_create",
        summary="Create fixed coupon",
        description="pending",
    )
}


fixed_coupon_detail_schema = {
    "get": extend_schema(
        operation_id="fixed_coupon_detail_retrieve",
        summary="Get fixed coupon",
        description="pending",
    ),
    "put": extend_schema(
        operation_id="fixed_coupon_detail_update",
        summary="Update fixed coupon",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="fixed_coupon_detail_destroy",
        summary="Delete fixed coupon",
        description="pending",
    )
}


percentage_coupon_list_schema = {
    "get": extend_schema(
        operation_id="percentage_coupon_list_retrieve",
        summary="Get percentage coupons",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="percentage_coupon_list_create",
        summary="Create percentage coupon",
        description="pending",
    )
}


percentage_coupon_detail_schema = {
    "get": extend_schema(
        operation_id="percentage_coupon_detail_retrieve",
        summary="Get percentage coupon",
        description="pending",
    ),
    "put": extend_schema(
        operation_id="percentage_coupon_detail_update",
        summary="Update percentage coupon",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="percentage_coupon_detail_destroy",
        summary="Delete percentage coupon",
        description="pending",
    )
}
