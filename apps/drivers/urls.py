"""URLs for Drivers App."""

from django.urls import path

from .views import (
    DriverCreateView,
    DriverProfileView,
    DriverResourceRequestView,
    DriverResourceHistoryView,
)


urlpatterns = [
    path(
        "api/v1/drivers/",
        DriverCreateView.as_view(),
    ),
    path(
        "api/v1/drivers/profile/",
        DriverProfileView.as_view(),
    ),
    path(
        "api/v1/drivers/request/",
        DriverResourceRequestView.as_view(),
    ),
    path(
        "api/v1/drivers/history/",
        DriverResourceHistoryView.as_view(),
    ),
]
