"""URLs for Orders App."""

from django.urls import path

from .views import (
    OrderListView, OrderDetailView, OrderItemListView, OrderItemDetailView)


urlpatterns = [
    path("api/v1/orders/", OrderListView.as_view()),
    path("api/v1/orders/<uuid:order_id>/", OrderDetailView.as_view()),
    path("api/v1/orders/<uuid:order_id>/items/", OrderItemListView.as_view()),
    path("api/v1/orders/<uuid:order_id>/items/<uuid:item_id>",
         OrderItemDetailView.as_view()),
]
