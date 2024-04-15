"""URLs for Orders App."""

from django.urls import path

from .views import OrderListView


urlpatterns = [
    path("api/v1/orders/", OrderListView)
]
