"""Routers for Promotions App."""

from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CheckCouponView
from .viewsets import PromotionViewSet, FixedCoponViewSet, PercentageCoponViewSet

router = DefaultRouter()
router.register(
    r"promotions",
    PromotionViewSet,
    basename="promotion",
)
router.register(
    r"fixed_coupons",
    FixedCoponViewSet,
    basename="fixed_coupon",
)
router.register(
    r"percentaje_coupons",
    PercentageCoponViewSet,
    basename="percentaje_coupon",
)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path(
        "api/v1/coupons/check/",
        CheckCouponView.as_view(),
    ),
]
