"""Routers for Restaurants App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .viewsets import RestaurantViewSet, CategoryViewSet, RestaurantReviewViewSet

router = DefaultRouter()
router.register(r"restaurants", RestaurantViewSet, basename="restaurant")

nested_router = NestedSimpleRouter(router, r"restaurants", lookup="restaurant")

nested_router.register(
    r"reviews",
    RestaurantReviewViewSet,
    basename="restaurant-review",
)
nested_router.register(
    r"categories",
    CategoryViewSet,
    basename="restaurant-category",
)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(nested_router.urls)),
]
