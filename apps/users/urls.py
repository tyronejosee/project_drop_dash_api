"""Urls for Users App."""

from django.urls import path, include

from .views import UserReviewsView, UserOrdersView, UserHistoryView


urlpatterns = [
    path(
        "api/v1/",
        include("djoser.urls"),
    ),
    path(
        "api/v1/tokens/",
        include("djoser.urls.jwt"),
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
        "api/v1/accounts/<str:pk>/history/",
        UserHistoryView.as_view(),
    ),
]
