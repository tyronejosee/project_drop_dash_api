"""Routers for Home App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import PageViewSet, KeywordViewSet

router = DefaultRouter()
router.register(r"pages", PageViewSet, basename="page")
router.register(r"keywords", KeywordViewSet, basename="keyword")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
