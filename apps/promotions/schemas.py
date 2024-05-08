"""Schemas for Promotions App."""

from drf_spectacular.utils import extend_schema

from .serializers import PromotionSerializer


promotion_list_schema = {
    "get": extend_schema(
        operation_id="promotion_list_retrieve",
        summary="Get promotions",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="promotion_list_create",
        summary="Create promotion",
        description="pending",
        responses={
            201: PromotionSerializer(),
            400: None
        }
    )
}


promotion_detail_schema = {
    "get": extend_schema(
        operation_id="promotion_detail_retrieve",
        summary="Get promotion",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="promotion_detail_destroy",
        summary="Delete promotion",
        description="pending",
    )
}
