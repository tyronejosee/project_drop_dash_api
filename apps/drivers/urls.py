"""URLs for Drivers App."""

from django.urls import path

from .views import DriverListAPIView, DriverMeAPIView


urlpatterns = [
    path("api/v1/drivers/me/", DriverMeAPIView.as_view()),
    path("api/v1/drivers/", DriverListAPIView.as_view())
]
