"""Schemas for Restaurants App."""

from drf_spectacular.utils import extend_schema, OpenApiResponse

from apps.reviews.serializers import ReviewReadSerializer, ReviewWriteSerializer
from apps.orders.serializers import OrderReadSerializer
from .serializers import (
    RestaurantReadSerializer,
    RestaurantWriteSerializer,
    RestaurantMinimalSerializer,
    CategoryReadSerializer,
    CategoryWriteSerializer,
    CategoryMinimalSerializer,
    FoodReadSerializer,
    FoodWriteSerializer,
    FoodMinimalSerializer,
)


restaurant_schemas = {
    "list": extend_schema(
        summary="Get Several Restaurants",
        description="Get a list of all available restaurants.",
        responses={
            200: OpenApiResponse(
                RestaurantMinimalSerializer(many=True), description="OK"
            ),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["restaurants"],
    ),
    "create": extend_schema(
        summary="Create a Restaurant",
        description="Create a new restaurant. The `user_id` is created by default, based on `request.user`, only for `IsClient` or `IsAdministrator` users.",
        request=RestaurantWriteSerializer,
        responses={
            201: OpenApiResponse(RestaurantWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
        },
        tags=["restaurants"],
    ),
    "retrieve": extend_schema(
        summary="Get a Restaurant",
        description="Get detailed information about a specific restaurant.",
        responses={
            200: OpenApiResponse(RestaurantReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["restaurants"],
    ),
    "update": extend_schema(
        summary="Update a Restaurant",
        description="Update all fields of a specific restaurant, only for `IsPartner` or `IsAdministrator` users.",
        request=RestaurantWriteSerializer,
        responses={
            200: OpenApiResponse(RestaurantWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["restaurants"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Restaurant",
        description="Update some fields of a specific restaurant, only for `IsPartner` or `IsAdministrator` users.",
        request=RestaurantWriteSerializer,
        responses={
            200: OpenApiResponse(RestaurantWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["restaurants"],
    ),
    "destroy": extend_schema(
        summary="Remove a Restaurant",
        description="Remove a specific restaurant, only for `IsPartner` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["restaurants"],
    ),
    "get_orders": extend_schema(
        summary="Get orders from a restaurant",
        description="This endpoint retrieves all orders associated with a specific restaurant identified by its ID, only for `IsPartner` or `IsAdministrator` users",
        responses={
            200: OpenApiResponse(OrderReadSerializer(many=True), description="OK"),
            400: OpenApiResponse(
                description="Bad Request (No orders found for this restaurant.)"
            ),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["restaurants"],
    ),
    "get_pending_verification": extend_schema(
        summary="Retrieve Restaurants Pending Verification",
        description="Retrieve a list of restaurants that are pending verification, only for `IsSupport` or `IsAdministrator` users",
        responses={
            200: OpenApiResponse(RestaurantReadSerializer(many=True), description="OK"),
            404: OpenApiResponse(description="Not Found (No restaurants found.)"),
        },
        tags=["restaurants"],
    ),
}


category_schemas = {
    "list": extend_schema(
        summary="Get all Categories of a Restaurant",
        description="Get a list of all available categories.",
        responses={
            200: OpenApiResponse(
                CategoryMinimalSerializer(many=True), description="OK"
            ),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["categories"],
    ),
    "create": extend_schema(
        summary="Create a Category of a Restaurant",
        description="Create a new category, only for `IsPartner` or `IsAdministrator` users.",
        request=CategoryWriteSerializer,
        responses={
            201: OpenApiResponse(CategoryWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(
                description="Forbidden (You do not have permission to add categories to this restaurant.)"
            ),
        },
        tags=["categories"],
    ),
    "retrieve": extend_schema(
        summary="Get a Category of a Restaurant",
        description="Get detailed information about a specific category.",
        responses={
            200: OpenApiResponse(CategoryReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["categories"],
    ),
    "update": extend_schema(
        summary="Update a Category of a Restaurant",
        description="Update all fields of a specific category, only for `IsPartner` or `IsAdministrator` users.",
        request=CategoryWriteSerializer,
        responses={
            200: OpenApiResponse(CategoryWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(
                description="Forbidden (You do not have permission to update this category.)"
            ),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["categories"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Category of a Restaurant",
        description="Update some fields of a specific category, only for `IsPartner` or `IsAdministrator` users.",
        request=CategoryWriteSerializer,
        responses={
            200: OpenApiResponse(CategoryWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(
                description="Forbidden (You do not have permission to update this category.)"
            ),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["categories"],
    ),
    "destroy": extend_schema(
        summary="Remove a Category of a Restaurant",
        description="Remove a specific category, only for `IsPartner` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(
                description="Forbidden (You do not have permission to delete this category.)"
            ),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["categories"],
    ),
}


food_schemas = {
    "list": extend_schema(
        summary="Get Several Foods of a Restaurant",
        description="Get a list of all available foods.",
        responses={
            200: OpenApiResponse(FoodMinimalSerializer(many=True), description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["foods"],
    ),
    "create": extend_schema(
        summary="Create a Food of a Restaurant",
        description="Create a new food, only for `IsPartner` or `IsAdministrator` users.",
        request=FoodWriteSerializer,
        responses={
            201: OpenApiResponse(FoodWriteSerializer, description="Created"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(
                description="Forbidden (You do not have permission to add foods to this restaurant.)"
            ),
        },
        tags=["foods"],
    ),
    "retrieve": extend_schema(
        summary="Get a Food of a Restaurant",
        description="Get detailed information about a specific food.",
        responses={
            200: OpenApiResponse(FoodReadSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            404: OpenApiResponse(description="Not Found"),
        },
        auth=[],
        tags=["foods"],
    ),
    "update": extend_schema(
        summary="Update a Food of a Restaurant",
        description="Update all fields of a specific food, only for `IsPartner` or `IsAdministrator` users.",
        request=FoodWriteSerializer,
        responses={
            200: OpenApiResponse(FoodWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(
                description="Forbidden (You do not have permission to update this food.)"
            ),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["foods"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Food of a Restaurant",
        description="Update some fields of a specific food, only for `IsPartner` or `IsAdministrator` users.",
        request=FoodWriteSerializer,
        responses={
            200: OpenApiResponse(FoodWriteSerializer, description="OK"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(
                description="Forbidden (You do not have permission to update this food.)"
            ),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["foods"],
    ),
    "destroy": extend_schema(
        summary="Remove a Food of a Restaurant",
        description="Remove a specific food, only for `IsPartner` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description="Bad Request"),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(
                description="Forbidden (You do not have permission to delete this food.)"
            ),
            404: OpenApiResponse(description="Not Found"),
        },
        tags=["foods"],
    ),
}


restaurant_review_schemas = {
    "list": extend_schema(
        summary="Get Several Restaurant Reviews",
        description="Get a list of all available restaurant reviews.",
        responses={
            200: OpenApiResponse(
                response=ReviewReadSerializer(many=True),
                description="OK (List of reviews successfully retrieved)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Invalid request data)",
            ),
            404: OpenApiResponse(
                description="Not Found (Reviews not found)",
            ),
        },
        auth=[],
        tags=["reviews"],
    ),
    "create": extend_schema(
        summary="Create a Restaurant Review",
        description="Create a new restaurant review, only for `IsClient` or `IsAdministrator` users.",
        request=ReviewWriteSerializer,
        responses={
            201: OpenApiResponse(
                response=ReviewWriteSerializer,
                description="Created (Review successfully created)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Only one review per user is allowed)",
            ),
            401: OpenApiResponse(
                description="Unauthorized (Authentication credentials were not provided)"
            ),
            403: OpenApiResponse(
                description="Forbidden (You do not have permission to perform this action)"
            ),
        },
        tags=["reviews"],
    ),
    "retrieve": extend_schema(
        summary="Get a Restaurant Review",
        description="Get detailed information about a specific restaurant review.",
        responses={
            200: OpenApiResponse(
                response=ReviewReadSerializer,
                description="OK (Review details successfully retrieved)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Invalid request data)",
            ),
            404: OpenApiResponse(
                description="Not Found (Review not found)",
            ),
        },
        auth=[],
        tags=["reviews"],
    ),
    "update": extend_schema(
        summary="Update a Restaurant Review",
        description="Update all fields of a specific restaurant review, only for `IsClient` or `IsAdministrator` users.",
        request=ReviewWriteSerializer,
        responses={
            200: OpenApiResponse(
                ReviewWriteSerializer, description="OK (Review successfully updated)"
            ),
            400: OpenApiResponse(
                description="Bad Request (Invalid request data)",
            ),
            401: OpenApiResponse(
                description="Unauthorized (Authentication credentials were not provided)"
            ),
            403: OpenApiResponse(
                description="Forbidden (You can only modify your own reviews)"
            ),
            404: OpenApiResponse(
                description="Not Found (Review not found)",
            ),
        },
        tags=["reviews"],
    ),
    "partial_update": extend_schema(
        summary="Partial Update a Restaurant Review",
        description="Update some fields of a specific restaurant review, only for `IsClient` or `IsAdministrator` users.",
        request=ReviewWriteSerializer,
        responses={
            200: OpenApiResponse(
                ReviewWriteSerializer,
                description="OK (Review successfully partially updated)",
            ),
            400: OpenApiResponse(
                description="Bad Request (Invalid request data)",
            ),
            401: OpenApiResponse(
                description="Unauthorized (Authentication credentials were not provided)"
            ),
            403: OpenApiResponse(
                description="Forbidden (You can only modify your own reviews)"
            ),
            404: OpenApiResponse(
                description="Not Found (Reviews not found)",
            ),
        },
        tags=["reviews"],
    ),
    "destroy": extend_schema(
        summary="Remove a Restaurant Review",
        description="Remove a specific restaurant review, only for `IsClient` or `IsAdministrator` users.",
        responses={
            204: OpenApiResponse(
                description="No Content (Review successfully removed)"
            ),
            400: OpenApiResponse(
                description="Bad Request (Invalid request data)",
            ),
            401: OpenApiResponse(
                description="Unauthorized (Authentication credentials were not provided)"
            ),
            403: OpenApiResponse(
                description="Forbidden (You can only delete your own reviews)"
            ),
            404: OpenApiResponse(
                description="Not Found (Review not found)",
            ),
        },
        tags=["reviews"],
    ),
}
