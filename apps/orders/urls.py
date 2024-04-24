"""URLs for Orders App."""

from django.urls import path

from .views import OrderListView


urlpatterns = [
    path("api/v1/orders/", OrderListView)

    # GET / api/orders
    # POST / api/orders
    # GET / api/orders/{order_id}
    # PUT / api/orders/{order_id}
    # DELETE / api/orders/{order_id}

    # GET / api/orders/{order_id}/items
    # GET / api/orders/{order_id}/items/{item_id}
    # POST / api/orders/{order_id}/items
    # PUT / api/orders/{order_id}/items/{item_id}
    # DELETE / api/orders/{order_id}/items/{item_id}
]
