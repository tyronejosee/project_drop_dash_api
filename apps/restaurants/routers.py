"""Routers for Restaurants App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import RestaurantViewSet

router = DefaultRouter()
router.register(r"restaurants", RestaurantViewSet, basename="restaurant")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
