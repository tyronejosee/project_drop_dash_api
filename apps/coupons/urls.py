"""URLs for Coupons App."""

from django.urls import path

from .views import CheckCouponAPIView


urlpatterns = [
    path("api/v1/coupons/check-coupon/", CheckCouponAPIView.as_view())
]
