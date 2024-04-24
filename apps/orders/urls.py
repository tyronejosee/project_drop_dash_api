"""URLs for Orders App."""

from django.urls import path

from .views import OrderListView, OrderDetailView, OrderItemListView


urlpatterns = [
    path("api/v1/orders/", OrderListView.as_view()),
    path("api/v1/orders/<uuid:order_id>/", OrderDetailView.as_view()),
    path("api/v1/orders/<uuid:order_id>/items/", OrderItemListView.as_view()),
]

# Endpoints

# GET / api/orders
# POST / api/orders
# GET / api/orders/{order_id}
# PUT / api/orders/{order_id}
# DELETE / api/orders/{order_id}

# GET / api/orders/{order_id}/items
# POST / api/orders/{order_id}/items
# GET / api/orders/{order_id}/items/{item_id}
# PUT / api/orders/{order_id}/items/{item_id}
# DELETE / api/orders/{order_id}/items/{item_id}
