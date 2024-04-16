"""URLs for Drivers App."""

from django.urls import path

from .views import DriverListAPIView, DriverDetailAPIView


urlpatterns = [
    path("api/v1/drivers/", DriverListAPIView.as_view()),
    path("api/v1/drivers/<uuid:driver_id>/", DriverDetailAPIView.as_view()),

    # path("api/v1/drivers/{driver_id}/orders",) GET
    # path("api/v1/drivers/{driver_id}/assign-order/{order_id}",) POST
    # path("api/v1/drivers/{driver_id}/order-history",) GET
    # path("api/v1/drivers/{driver_id}/availability",) PUT
]
