"""Urls for Users App."""

from django.urls import path, include


urlpatterns = [
    path("api/v1/", include("djoser.urls")),
    path("api/v1/tokens/", include("djoser.urls.jwt")),
    path("api/v1/socials/", include("djoser.social.urls")),
]
