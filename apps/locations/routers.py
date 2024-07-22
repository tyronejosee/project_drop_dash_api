"""Routers for Locations App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import CountryViewSet, StateViewSet, CityViewSet

router = DefaultRouter()
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"states", StateViewSet, basename="state")
router.register(r"cities", CityViewSet, basename="city")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
