"""Schemas for Promotions App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter

from .serializers import (
    PromotionReadSerializer,
    PromotionWriteSerializer,
    FixedCouponReadSerializer,
    FixedCouponWriteSerializer,
    PercentageCouponReadSerializer,
    PercentageCouponWriteSerializer,
)

check_coupon_schemas = {
    "get": extend_schema(
        summary="Check a Coupon Code",
        description="Check the validity of a coupon code, only for `IsMarketing` or `IsAdministrator` users.",
        parameters=[
            OpenApiParameter(
                name="coupon_code",
                description="The coupon code to be validated",
                required=True,
                type=str,
                location=OpenApiParameter.QUERY,
            ),
        ],
        responses={
            200: OpenApiResponse(
                description="OK - Returns a FixedCoupon or PercentageCoupon serializer depending on the type of coupon found.",
            ),
            400: OpenApiResponse(description="Bad request, coupon code is required"),
            404: OpenApiResponse(description="Coupon code not found"),
            500: OpenApiResponse(description="Internal server error"),
        },
        tags=["coupons"],
    ),
}


promotion_schemas = {
    "list": extend_schema(
        summary="Get Several Promotions",
        description="Get a list of all available promotions, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(PromotionReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["promotions"],
    ),
    "create": extend_schema(
        summary="Create a Promotion",
        description="Create a new promotion, only for `IsMarketing` or `IsAdministrator` users.",
        request=PromotionWriteSerializer,
        responses={
            201: OpenApiResponse(PromotionWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["promotions"],
    ),
    "retrieve": extend_schema(
        summary="Get a Promotion",
        description="Get detailed information about a specific promotion, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(PromotionReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["promotions"],
    ),
    "update": extend_schema(
        summary="Update a Promotion",
        description="Update all fields of a specific promotion, only for `IsMarketing` or `IsAdministrator` users.",
        request=PromotionWriteSerializer,
        responses={
            200: OpenApiResponse(PromotionWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["promotions"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Promotion",
        description="Update some fields of a specific promotion, only for `IsMarketing` or `IsAdministrator` users.",
        request=PromotionWriteSerializer,
        responses={
            200: OpenApiResponse(PromotionWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["promotions"],
    ),
    "destroy": extend_schema(
        summary="Remove a Promotion",
        description="Remove a specific promotion, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["promotions"],
    ),
}


fixed_coupon_schemas = {
    "list": extend_schema(
        summary="Get Several FixedCoupons",
        description="Get a list of all available fixed_coupons, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(
                FixedCouponReadSerializer(many=True), description="OK"
            ),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["coupons"],
    ),
    "create": extend_schema(
        summary="Create a FixedCoupon",
        description="Create a new fixed_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        request=FixedCouponWriteSerializer,
        responses={
            201: OpenApiResponse(FixedCouponWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["coupons"],
    ),
    "retrieve": extend_schema(
        summary="Get a FixedCoupon",
        description="Get detailed information about a specific fixed_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(FixedCouponReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["coupons"],
    ),
    "update": extend_schema(
        summary="Update a FixedCoupon",
        description="Update all fields of a specific fixed_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        request=FixedCouponWriteSerializer,
        responses={
            200: OpenApiResponse(FixedCouponWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["coupons"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a FixedCoupon",
        description="Update some fields of a specific fixed_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        request=FixedCouponWriteSerializer,
        responses={
            200: OpenApiResponse(FixedCouponWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["coupons"],
    ),
    "destroy": extend_schema(
        summary="Remove a FixedCoupon",
        description="Remove a specific fixed_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["coupons"],
    ),
}


percentage_coupon_schemas = {
    "list": extend_schema(
        summary="Get Several PercentageCoupons",
        description="Get a list of all available percentage_coupons, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(
                PercentageCouponReadSerializer(many=True), description="OK"
            ),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["coupons"],
    ),
    "create": extend_schema(
        summary="Create a PercentageCoupon",
        description="Create a new percentage_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        request=PercentageCouponWriteSerializer,
        responses={
            201: OpenApiResponse(
                PercentageCouponWriteSerializer, description="Created"
            ),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["coupons"],
    ),
    "retrieve": extend_schema(
        summary="Get a PercentageCoupon",
        description="Get detailed information about a specific percentage_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(PercentageCouponReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["coupons"],
    ),
    "update": extend_schema(
        summary="Update a PercentageCoupon",
        description="Update all fields of a specific percentage_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        request=PercentageCouponWriteSerializer,
        responses={
            200: OpenApiResponse(PercentageCouponWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["coupons"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a PercentageCoupon",
        description="Update some fields of a specific percentage_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        request=PercentageCouponWriteSerializer,
        responses={
            200: OpenApiResponse(PercentageCouponWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["coupons"],
    ),
    "destroy": extend_schema(
        summary="Remove a PercentageCoupon",
        description="Remove a specific percentage_coupon, only for `IsMarketing` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["coupons"],
    ),
}
