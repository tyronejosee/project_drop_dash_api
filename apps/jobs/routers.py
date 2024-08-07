"""Routers for Jobs App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import PositionViewSet, WorkerViewSet, ApplicantViewSet

router = DefaultRouter()
router.register(r"positions", PositionViewSet, basename="position")
router.register(r"workers", WorkerViewSet, basename="worker")
router.register(r"applicants", ApplicantViewSet, basename="applicant")

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
