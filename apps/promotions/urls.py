"""URLs for Promotions App."""

from django.urls import path

from .views import (
    PromotionListView,
    PromotionDetailView,
    PromotionSearchView,
    FixedCouponListView,
    FixedCouponDetailView,
    PercentageCouponListView,
    PercentageCouponDetailView,
    CheckCouponView,
)


urlpatterns = [
    path(
        "api/v1/promotions/",
        PromotionListView.as_view(),
    ),
    path(
        "api/v1/promotions/<uuid:promotion_id>/",
        PromotionDetailView.as_view(),
    ),
    path(
        "api/v1/promotions/search/",
        PromotionSearchView.as_view(),
    ),
    path(
        "api/v1/coupons/fixed-coupons/",
        FixedCouponListView.as_view(),
    ),
    path(
        "api/v1/coupons/fixed-coupons/<uuid:fixed_coupon_id>",
        FixedCouponDetailView.as_view(),
    ),
    path(
        "api/v1/coupons/percentage-coupons/",
        PercentageCouponListView.as_view(),
    ),
    path(
        "api/v1/coupons/percentage-coupons/<uuid:percentage_coupon_id>",
        PercentageCouponDetailView.as_view(),
    ),
    path(
        "api/v1/coupons/check-coupons/",
        CheckCouponView.as_view(),
    ),
]
