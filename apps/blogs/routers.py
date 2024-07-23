"""Routers for Blogs App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import PostViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="post")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
