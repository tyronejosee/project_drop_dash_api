"""Routers for Jobs App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import PositionViewSet

router = DefaultRouter()
router.register(r"positions", PositionViewSet, basename="position")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
