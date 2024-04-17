"""URLs for Restaurants App."""

from django.urls import path

from .views import RestaurantListAPIView, RestaurantDetailAPIView, RestaurantCategoriesAPIView


urlpatterns = [
    path("api/v1/restaurants/", RestaurantListAPIView.as_view()),
    path("api/v1/restaurants/<uuid:restaurant_id>/",
         RestaurantDetailAPIView.as_view()),
    path("api/v1/restaurants/<uuid:restaurant_id>/categories/",
         RestaurantCategoriesAPIView.as_view()),
]
