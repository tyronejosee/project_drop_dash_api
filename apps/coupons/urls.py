"""URLs for Coupons App."""

from django.urls import path

from .views import (
    FixedCouponListAPIView, FixedCouponDetailAPIView,
    PercentageCouponListAPIView, PercentageCouponDetailAPIView,
    CheckCouponAPIView
)


urlpatterns = [
    path("api/v1/coupons/fixed-coupons/", FixedCouponListAPIView.as_view()),
    path("api/v1/coupons/fixed-coupons/<uuid:fixed_coupon_id>",
         FixedCouponDetailAPIView.as_view()),
    path("api/v1/coupons/percentage-coupons/",
         PercentageCouponListAPIView.as_view()),
    path("api/v1/coupons/percentage-coupons/<uuid:percentage_coupon_id>",
         PercentageCouponDetailAPIView.as_view()),
    path("api/v1/coupons/check-coupons/", CheckCouponAPIView.as_view())
]
