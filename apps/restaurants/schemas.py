"""Schemas for Restaurants App."""

from drf_spectacular.utils import extend_schema


restaurant_list_schema = {
    "get": extend_schema(
        operation_id="restaurant_list_retrieve",
        summary="Get restaurants",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="restaurant_list_create",
        summary="Create restaurant",
        description="pending",
    )
}


restaurant_detail_schema = {
    "get": extend_schema(
        operation_id="restaurant_detail_retrieve",
        summary="Get restaurant",
        description="pending",
    ),
    "put": extend_schema(
        operation_id="restaurant_detail_update",
        summary="Update restaurant",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="restaurant_detail_destroy",
        summary="Delete restaurant",
        description="pending",
    )
}


restaurant_categories_schema = {
    "get": extend_schema(
        operation_id="restaurant_categories_retrieve",
        summary="Get categories from restaurant",
        description="pending",
    )
}


restaurant_foods_schema = {
    "get": extend_schema(
        operation_id="restaurant_foods_retrieve",
        summary="Get foods from restaurant",
        description="pending",
    )
}


category_list_schema = {
    "get": extend_schema(
        operation_id="category_list_retrieve",
        summary="Get categories",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="category_list_create",
        summary="Create category",
        description="pending",
    )
}


category_detail_schema = {
    "get": extend_schema(
        operation_id="category_detail_retrieve",
        summary="Get category",
        description="pending",
    ),
    "put": extend_schema(
        operation_id="category_detail_update",
        summary="Update category",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="category_detail_destroy",
        summary="Delete category",
        description="pending",
    )
}


food_list_schema = {
    "get": extend_schema(
        operation_id="food_list_retrieve",
        summary="Get foods",
        description="pending",
    ),
    "post": extend_schema(
        operation_id="food_list_create",
        summary="Create food",
        description="pending",
    )
}


food_detail_schema = {
    "get": extend_schema(
        operation_id="food_detail_retrieve",
        summary="Get food",
        description="pending",
    ),
    "put": extend_schema(
        operation_id="food_detail_update",
        summary="Update food",
        description="pending",
    ),
    "delete": extend_schema(
        operation_id="food_detail_destroy",
        summary="Delete food",
        description="pending",
    )
}
