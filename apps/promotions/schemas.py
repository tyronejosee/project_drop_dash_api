"""Schemas for Promotions App."""

from drf_spectacular.utils import extend_schema

from .serializers import PromotionReadSerializer, PromotionWriteSerializer


promotion_list_schema = {
    "get": extend_schema(
        operation_id="promotion_list_retrieve",
        summary="Get promotions",
        description="Get all promotions, the 'administrator' role is required",
        responses={200: PromotionReadSerializer(), 500: None},
    ),
    "post": extend_schema(
        operation_id="promotion_list_create",
        summary="Create promotion",
        description="Create a promotion, the 'administrator' role is required",
        responses={201: PromotionWriteSerializer(), 400: None},
    ),
}


promotion_detail_schema = {
    "get": extend_schema(
        operation_id="promotion_detail_retrieve",
        summary="Get promotion",
        description="Get a promotion, the 'administrator' role is required",
        responses={
            200: PromotionReadSerializer(),
        },
    ),
    "delete": extend_schema(
        operation_id="promotion_detail_destroy",
        summary="Delete promotion",
        description="Delete a promotion, the 'administrator' role is required",
        responses={
            204: None,
        },
    ),
}


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
    ),
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
    ),
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
    ),
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
    ),
}
