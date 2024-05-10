"""URLs for Restaurants App."""

from django.urls import path

from .views import (
    RestaurantListView, RestaurantDetailView,
    RestaurantCategoriesView, RestaurantFoodsView,)


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
]

# path(
#     "api/v1/categories/",
#     CategoryList.as_view()
# ),
# path(
#     "api/v1/categories/<uuid:category_id>/",
#     CategoryDetail.as_view()
# )
