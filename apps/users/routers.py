"""Routers for Users App."""

from django.urls import include
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from .viewsets import UserExtensionViewSet
from .views import (
    TokenObtainPairExtensionView,
    TokenRefreshExtensionView,
    TokenVerifyExtensionView,
    UserReviewsView,
    UserOrdersView,
    UserOrderReportsView,
    UserHistoryView,
)

router = DefaultRouter()
router.register(r"users", UserExtensionViewSet, basename="user")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    # path(
    #     "api/v1/",
    #     include("djoser.urls"),
    # ),
    # path(
    #     "api/v1/tokens/",
    #     include("djoser.urls.jwt"),
    # ),
    # djangorestframework-simplejwt urls
    re_path(
        r"^api/v1/jwt/create/?",
        TokenObtainPairExtensionView.as_view(),
        name="jwt-create",
    ),
    re_path(
        r"^api/v1/jwt/refresh/?",
        TokenRefreshExtensionView.as_view(),
        name="jwt-refresh",
    ),
    re_path(
        r"^api/v1/jwt/verify/?",
        TokenVerifyExtensionView.as_view(),
        name="jwt-verify",
    ),
    path(
        "api/v1/socials/",
        include("djoser.social.urls"),
    ),
    # Views urls
    path(
        "api/v1/accounts/reviews/",
        UserReviewsView.as_view(),
    ),
    path(
        "api/v1/accounts/orders/",
        UserOrdersView.as_view(),
    ),
    path(
        "api/v1/accounts/order_reports/",
        UserOrderReportsView.as_view(),
    ),
    path(
        "api/v1/accounts/<str:pk>/history/",
        UserHistoryView.as_view(),
    ),
]
