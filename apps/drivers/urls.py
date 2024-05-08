"""URLs for Drivers App."""

from django.urls import path

from .views import DriverListAPIView, DriverDetailAPIView


urlpatterns = [
    path(
        "api/v1/drivers/",
        DriverListAPIView.as_view()
    ),
    path(
        "api/v1/drivers/<uuid:driver_id>/",
        DriverDetailAPIView.as_view()
    ),

    # GET drivers/{driver_id}/orders
    # POST drivers/{driver_id}/assign_order
    # GET drivers/{driver_id}/order-history
    # PUT drivers/{driver_id}/availability
]
