"""URLs for Restaurants App."""

from django.urls import path

from .views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantSearchView,
    RestaurantReviewListView,
    RestaurantReviewDetailView,
    CategoryListView,
    CategoryDetailView,
    RestaurantOrderListView,
    FoodListView,
    FoodDetailView,
    FoodDeletedListView,
)


urlpatterns = [
    path(
        "api/v1/restaurants/",
        RestaurantListView.as_view(),
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/",
        RestaurantDetailView.as_view(),
    ),
    path(
        "api/v1/restaurants/search/",
        RestaurantSearchView.as_view(),
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/reviews/",
        RestaurantReviewListView.as_view(),
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/reviews/<uuid:review_id>/",
        RestaurantReviewDetailView.as_view(),
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/categories/",
        CategoryListView.as_view(),
    ),
    path(
        ("api/v1/restaurants/<uuid:restaurant_id>/categories/<uuid:category_id>/"),
        CategoryDetailView.as_view(),
    ),
    path(
        ("api/v1/restaurants/<uuid:restaurant_id>/orders/"),
        RestaurantOrderListView.as_view(),
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/foods/",
        FoodListView.as_view(),
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/foods/<uuid:food_id>/",
        FoodDetailView.as_view(),
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/foods/deleted/",
        FoodDeletedListView.as_view(),
    ),
]
