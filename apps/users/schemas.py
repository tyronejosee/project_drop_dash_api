"""Schemas for Users App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiParameter

from apps.orders.serializers import OrderReadSerializer, OrderReportReadSerializer
from apps.reviews.serializers import ReviewReadSerializer
from .serializers import (
    UserReadSerializer,
    UserWriteSerializer,
    UserMinimalSerializer,
    UserHistorySerializer,
)


user_schemas = {
    "list": extend_schema(
        summary="Get Several Users",
        description="Get a list of all available users.",
        responses={
            200: OpenApiResponse(UserMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["users"],
    ),
    "create": extend_schema(
        summary="Create a User",
        description="Create a new user, only for `IsClient` or `IsAdministrator` users.",
        request=UserWriteSerializer,
        responses={
            201: OpenApiResponse(UserWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["users"],
    ),
    "retrieve": extend_schema(
        summary="Get a User",
        description="Get detailed information about a specific user.",
        responses={
            200: OpenApiResponse(UserReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            404: OpenApiResponse(description="Not found"),
        },
        tags=["users"],
    ),
    "update": extend_schema(
        summary="Update a User",
        description="Update all fields of a specific user, only for `IsClient` or `IsAdministrator` users.",
        request=UserWriteSerializer,
        responses={
            200: OpenApiResponse(UserWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["users"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a User",
        description="Update some fields of a specific user, only for `IsClient` or `IsAdministrator` users.",
        request=UserWriteSerializer,
        responses={
            200: OpenApiResponse(UserWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["users"],
    ),
    "destroy": extend_schema(
        summary="Remove a User",
        description="Remove a specific user, only for `IsClient`.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["users"],
    ),
    "me": extend_schema(
        summary="Retrieve User Details",
        description="Retrieve the details of the current user (Get, update, partial update, delete).",
        tags=["users"],
    ),
    "activation": extend_schema(
        summary="Activate User Account",
        description="Activates a user account and sends a confirmation email if configured.",
        responses={
            204: OpenApiResponse(
                description="No Content (User account successfully activated)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Invalid request data)",
            ),
            404: OpenApiResponse(
                description="Not Found (User not found)",
            ),
        },
        tags=["users"],
    ),
    "resend_activation": extend_schema(
        summary="Resend Activation Email",
        description="Resends an activation email to the user if the user is not active and activation emails are enabled in the settings.",
        responses={
            204: OpenApiResponse(
                description="No Content (Activation email successfully sent)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Bad request or activation emails are disabled)",
            ),
        },
        tags=["users"],
    ),
    "set_password": extend_schema(
        summary="Set New Password",
        description="Sets a new password for the user and sends a confirmation email if configured. The user is logged out if configured, or the session is updated.",
        responses={
            204: OpenApiResponse(
                description="No Content (Password successfully updated)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Validation error in the provided password)",
            ),
        },
        tags=["users"],
    ),
    "reset_password": extend_schema(
        summary="Reset Password",
        description="Sends a password reset email to the user if the email address is associated with an active account.",
        responses={
            204: OpenApiResponse(
                description="No Content (Password reset email sent successfully)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Validation error in the provided email)",
            ),
            404: OpenApiResponse(
                description="Not Found (The email address is not associated with an active account)",
            ),
        },
        tags=["users"],
    ),
    "reset_password_confirm": extend_schema(
        summary="Confirm Password Reset",
        description="Confirms the password reset request and sets a new password for the user if the token is valid.",
        responses={
            204: OpenApiResponse(
                description="No Content (Password has been successfully reset)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Validation error in the provided data)",
            ),
            404: OpenApiResponse(
                description="Not Found (The token or user associated with the token is invalid)",
            ),
        },
        tags=["users"],
    ),
    "set_username": extend_schema(
        summary="Set Username",
        description="Updates the username of the current user. Sends a confirmation email if configured.",
        responses={
            204: OpenApiResponse(
                description="No Content (Username has been successfully updated)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Validation error in the provided data)",
            ),
        },
        tags=["users"],
    ),
    "reset_username": extend_schema(
        summary="Reset Username",
        description="Sends a username reset email to the user specified by their email address.",
        responses={
            204: OpenApiResponse(
                description="No Content (Username reset email has been sent)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Validation error in the provided data)",
            ),
        },
        tags=["users"],
    ),
    "reset_username_confirm": extend_schema(
        summary="Confirm Username Reset",
        description="Confirms the username reset request and sets a new username for the user. Requires a valid token.",
        responses={
            204: OpenApiResponse(
                description="No Content (Username has been successfully updated and a confirmation email has been sent)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Validation error or token is invalid)",
            ),
        },
        tags=["users"],
    ),
}


token_obtain_pair_schemas = {
    "post": extend_schema(
        summary="Token Obtain Pair",
        description="Endpoint to obtain a pair of JWT tokens (access and refresh) by providing valid user credentials.",
        tags=["tokens"],
    ),
}


token_refresh_schemas = {
    "post": extend_schema(
        summary="Token Refresh",
        description="Endpoint to refresh an access token by providing a valid refresh token.",
        tags=["tokens"],
    ),
}


token_verify_schemas = {
    "post": extend_schema(
        summary="Token Verify",
        description=(
            "Endpoint to verify the validity of a token."
            "This view indicates whether the provided token is valid but does not provide information on its fitness for a particular use."
        ),
        tags=["tokens"],
    ),
}

provider_auth_schemas = {
    "get": extend_schema(
        summary="Get Authorization URL",
        description=(
            "Provides the URL for authorization by interacting with the specified provider."
            "Validates the `redirect_uri` against allowed URIs and sets it in the session."
        ),
        tags=["socials"],
    ),
    "post": extend_schema(
        summary="Authenticate with Provider",
        description="Initiates authentication with the specified provider and returns the URL for authorization.",
        tags=["socials"],
    ),
}


user_review_schemas = {
    "get": extend_schema(
        summary="Get Reviews of Authenticated User",
        description="This endpoint returns a list of reviews created by the authenticated user, only for `IsClient` users.",
        responses={
            200: OpenApiResponse(
                response=ReviewReadSerializer(many=True),
                description="OK (List of reviews successfully retrieved)",
            ),
            404: OpenApiResponse(
                description="Not Found (Reviews not found)",
            ),
        },
        tags=["accounts"],
    ),
}

user_order_schemas = {
    "get": extend_schema(
        summary="Get Orders of Authenticated User",
        description="This endpoint returns a list of orders created by the authenticated user, only for `IsClient` users.",
        responses={
            200: OpenApiResponse(
                response=OrderReadSerializer(many=True),
                description="OK (List of orders successfully retrieved)",
            ),
            404: OpenApiResponse(
                description="Not Found (Orders not found)",
            ),
        },
        tags=["accounts"],
    ),
}


user_order_report_schemas = {
    "get": extend_schema(
        summary="Get Order Reports of Authenticated User",
        description="This endpoint returns a list of order reports created by the authenticated user, only for `IsClient` users.",
        responses={
            200: OpenApiResponse(
                response=OrderReportReadSerializer(many=True),
                description="OK (List of orders reports successfully retrieved)",
            ),
            404: OpenApiResponse(
                description="Not Found (Orders reports not found)",
            ),
        },
        tags=["accounts"],
    ),
}


user_history_schemas = {
    "get": extend_schema(
        summary="Get User History",
        description="This endpoint returns a history of actions performed by a specific user, identified by user ID, only for `IsAdministrator` users.",
        parameters=[
            OpenApiParameter(
                "id", description="ID of the user", required=True, type=int
            ),
        ],
        responses={
            200: OpenApiResponse(
                response=UserHistorySerializer(many=True),
                description="OK (List of user history successfully retrieved)",
            ),
            404: OpenApiResponse(
                description="Not Found (User not found)",
            ),
        },
        tags=["accounts"],
    ),
}
