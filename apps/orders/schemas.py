"""Schemas for Orders App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.deliveries.serializers import SignatureSerializer, FailedDeliverySerializer
from .serializers import (
    OrderReadSerializer,
    OrderWriteSerializer,
    OrderMinimalSerializer,
    OrderRatingWriteSerializer,
    OrderItemReadSerializer,
    OrderItemWriteSerializer,
)


order_schemas = {
    "list": extend_schema(
        summary="Get Several Orders",
        description="Get a list of all available orders, only for `IsClient` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(OrderMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["orders"],
    ),
    "create": extend_schema(
        summary="Create a Order",
        description="Create a new order, only for `IsClient` or `IsAdministrator` users.",
        request=OrderWriteSerializer,
        responses={
            201: OpenApiResponse(OrderWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["orders"],
    ),
    "retrieve": extend_schema(
        summary="Get a Order",
        description="Get detailed information about a specific order, only for `IsClient` or `IsAdministrator` users.",
        responses={
            200: OpenApiResponse(OrderReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        auth=[],
        tags=["orders"],
    ),
    "update": extend_schema(
        summary="Update a Order",
        description="Update all fields of a specific order, only for `IsClient` or `IsAdministrator` users.",
        request=OrderWriteSerializer,
        responses={
            200: OpenApiResponse(OrderWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["orders"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Order",
        description="Update some fields of a specific order, only for `IsClient` or `IsAdministrator` users.",
        request=OrderWriteSerializer,
        responses={
            200: OpenApiResponse(OrderWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["orders"],
    ),
    "destroy": extend_schema(
        summary="Remove a Order",
        description="Remove a specific order, only for `IsClient` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["orders"],
    ),
    "report_order": extend_schema(
        summary="Report an Order",
        description="Allows drivers to report an order by its ID. The request should include necessary details for the report, only for `IsClient` or `IsAdministrator` users.",
        request=None,
        responses={
            201: OpenApiResponse(
                description="Your report has been submitted successfully."
            ),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            409: OpenApiResponse(description="You have already reported this order."),
        },
        tags=["orders"],
    ),
    "assign_driver": extend_schema(
        summary="Assign a Driver to an Order",
        description="Assigns an available driver to an order. Only available drivers who are verified and active will be considered. If no drivers are available, an error will be returned, only for `IsDispatcher` or `IsAdministrator` users.",
        request=None,
        responses={
            200: OpenApiResponse(
                description="Driver `driver.id` assigned to order `order.id`."
            ),
            400: OpenApiResponse(
                description="There are no drivers available for assignment."
            ),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["orders"],
    ),
    "accept_order": extend_schema(
        summary="Accept an Order Assignment",
        description="Marks a specific order assignment as accepted by a driver. The driver must have a pending assignment for the order. If no such assignment exists, an error is returned. only for `IsDriver` or `IsAdministrator` users.",
        request=None,
        responses={
            200: OpenApiResponse(description="The order `order.id` was accepted."),
            400: OpenApiResponse(
                description="No pending assignment found for this driver."
            ),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
            500: OpenApiResponse(description="Internal Server Error"),
        },
        tags=["orders"],
    ),
    "reject_order": extend_schema(
        summary="Reject an Order Assignment",
        description="Marks a specific order assignment as rejected by a driver. The driver must have an assignment for the order. If the assignment does not exist or cannot be updated, an error is returned. only for `IsDriver` or `IsAdministrator` users.",
        request=None,
        responses={
            200: OpenApiResponse(description="The order `order_id` was rejected."),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
            500: OpenApiResponse(description="Internal Server Error"),
        },
        tags=["orders"],
    ),
    "picked_up_order": extend_schema(
        summary="Mark Order as Picked Up",
        description="Marks a specific order assignment as rejected by a driver. The driver must have an assignment for the order. If the assignment does not exist or cannot be updated, an error is returned. only for `IsDriver` or `IsAdministrator` users.",
        request=None,
        responses={
            200: OpenApiResponse(
                description="Delivery status was changed to 'Picked Up'."
            ),
            400: OpenApiResponse(
                description="Delivery with status pending cannot be marked."
            ),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
            409: OpenApiResponse(
                description="Delivery has already been marked as 'Picked Up'."
            ),
        },
        tags=["orders"],
    ),
    "delivered_order": extend_schema(
        summary="Mark Order as Delivered",
        description="Marks a delivery status as 'Delivered'. The delivery must have been marked as 'Picked Up' before it can be marked as 'Delivered'. A valid signature is required to complete the delivery. only for `IsDriver` or `IsAdministrator` users.",
        request=SignatureSerializer,
        responses={
            200: OpenApiResponse(description="Order successfully delivered."),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
            409: OpenApiResponse(
                description="The status could not be changed, please try again."
            ),
        },
        tags=["orders"],
    ),
    "failed_order": extend_schema(
        summary="Mark Order as Failed",
        description="Marks a delivery status as 'Failed'. The delivery must have been either 'Assigned' or 'Picked Up' before it can be marked as 'Failed'. A reason for failure is required. only for `IsDriver` or `IsAdministrator` users.",
        request=FailedDeliverySerializer,
        responses={
            201: OpenApiResponse(description="Failed delivery recorded successfully."),
            400: OpenApiResponse(
                description="The status could not be changed, please try again."
            ),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["orders"],
    ),
    "rate_order": extend_schema(
        summary="Rate an Order",
        description="Allows a client to rate an order. The rating must be provided in the request body. The client must be authenticated to perform this action. only for `IsClient` or `IsAdministrator` users.",
        request=OrderRatingWriteSerializer,
        responses={
            201: OpenApiResponse(
                OrderRatingWriteSerializer,
                description="OK",
            ),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["orders"],
    ),
}


order_item_schemas = {
    "list": extend_schema(
        summary="Get Several OrderItems",
        description="Get a list of all available order_items.",
        responses={
            200: OpenApiResponse(OrderItemReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["orders"],
    ),
    "create": extend_schema(
        summary="Create a OrderItem",
        description="Create a new order_item for order, only for `IsClient` or `IsAdministrator` users.",
        request=OrderItemWriteSerializer,
        responses={
            201: OpenApiResponse(OrderItemWriteSerializer, description="Created"),
            400: OpenApiResponse(
                description="The combination of order and food already exists."
            ),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["orders"],
    ),
    "retrieve": extend_schema(
        summary="Get a OrderItem",
        description="Get detailed information about a specific order_item.",
        responses={
            200: OpenApiResponse(OrderItemReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["orders"],
    ),
    "update": extend_schema(
        summary="Update a OrderItem",
        description="Update all fields of a specific order_item, only for `IsClient` or `IsAdministrator` users.",
        request=OrderItemWriteSerializer,
        responses={
            200: OpenApiResponse(OrderItemWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["orders"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a OrderItem",
        description="Update some fields of a specific order_item, only for `IsClient` or `IsAdministrator` users.",
        request=OrderItemWriteSerializer,
        responses={
            200: OpenApiResponse(OrderItemWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["orders"],
    ),
    "destroy": extend_schema(
        summary="Remove a OrderItem",
        description="Remove a specific order_item, only for `IsClient` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["orders"],
    ),
}
