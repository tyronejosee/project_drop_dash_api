"""URLs for Orders App."""

from django.urls import path

from .views import OrderCreateView


urlpatterns = [
    path(
        "api/v1/orders/",
        OrderCreateView.as_view()
    )
]
