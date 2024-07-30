"""Routers for Drivers App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import DriverViewSet

router = DefaultRouter()
router.register(r"drivers", DriverViewSet, basename="driver")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
