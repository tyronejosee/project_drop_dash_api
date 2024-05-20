"""URLs for Drivers App."""

from django.urls import path

from .views import (
    DriverListView,
    DriverDetailView,
    DriverResourceRequestView,
    DriverResourceHistoryView,
)


urlpatterns = [
    path(
        "api/v1/drivers/",
        DriverListView.as_view(),
    ),
    path(
        "api/v1/drivers/<uuid:driver_id>/",
        DriverDetailView.as_view(),
    ),
    path(
        "api/v1/drivers/request/",
        DriverResourceRequestView.as_view(),
    ),
    path(
        "api/v1/drivers/history/",
        DriverResourceHistoryView.as_view(),
    ),
    # GET drivers/{driver_id}/orders
    # POST drivers/{driver_id}/assign_order
    # GET drivers/{driver_id}/order-history
    # PUT drivers/{driver_id}/availability
]
