"""URLs for Coupons App."""

from django.urls import path

from .views import FixedCouponListAPIView, CheckCouponAPIView


urlpatterns = [
    path("api/v1/coupons/fixed-coupons/", FixedCouponListAPIView.as_view()),
    path("api/v1/coupons/check-coupons/", CheckCouponAPIView.as_view())
]
