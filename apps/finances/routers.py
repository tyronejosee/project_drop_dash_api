"""Routers for Finances App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import RevenueViewSet

router = DefaultRouter()
router.register(r"revenues", RevenueViewSet, basename="revenue")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
