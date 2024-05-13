"""URLs for Restaurants App."""

from django.urls import path

from .views import (
    RestaurantListView, RestaurantDetailView, RestaurantCategoriesView,
    RestaurantFoodsView, FoodListView, FoodDetailView, FoodDeletedListView)


urlpatterns = [
    path(
        "api/v1/restaurants/",
        RestaurantListView.as_view()
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/",
        RestaurantDetailView.as_view()
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/categories/",
        RestaurantCategoriesView.as_view()
    ),
    path(
        "api/v1/restaurants/<uuid:restaurant_id>/foods/",
        RestaurantFoodsView.as_view()
    ),
    path(
        "api/v1/foods/",
        FoodListView.as_view()
    ),
    path(
        "api/v1/foods/<uuid:food_id>/",
        FoodDetailView.as_view()
    ),
    path(
        "api/v1/foods/deleted/",
        FoodDeletedListView.as_view()
    ),
]
