"""URLs for Restaurants App."""

from django.urls import path

from .views import RestaurantListAPIView, RestaurantDetailAPIView


urlpatterns = [
    path("api/v1/restaurants/", RestaurantListAPIView.as_view(), name="store-list"),
    path("api/v1/restaurants/<uuid:restaurant_id>/",
         RestaurantDetailAPIView.as_view(), name="store-detail"),
]
