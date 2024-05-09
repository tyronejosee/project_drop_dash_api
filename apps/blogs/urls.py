"""URLs for Blogs App."""

from django.urls import path

from .views import PostListView


urlpatterns = [
    path(
        "api/v1/posts/",
        PostListView.as_view()
    )
]
