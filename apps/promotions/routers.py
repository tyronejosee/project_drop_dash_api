"""Routers for Promotions App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import PromotionViewSet

router = DefaultRouter()
router.register(r"promotions", PromotionViewSet, basename="promotion")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
