"""URLs for Home App."""

from django.urls import path

from .views import KeywordView


urlpatterns = [
    path(
        "api/v1/keywords/",
        KeywordView.as_view(),
    ),
]
