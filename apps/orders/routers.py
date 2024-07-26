"""Routers for Orders App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter

from .viewsets import OrderViewSet, OrderItemViewSet

router = DefaultRouter()
router.register(r"orders", OrderViewSet, basename="order")

orders_router = NestedSimpleRouter(router, r"orders", lookup="order")
orders_router.register(r"items", OrderItemViewSet, basename="order-items")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/", include(orders_router.urls)),
]
