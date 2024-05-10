"""URLs for Blogs App."""

from django.urls import path

from .views import PostListView, TagListView


urlpatterns = [
    path(
        "api/v1/posts/",
        PostListView.as_view()
    ),
    path(
        "api/v1/posts/tags/",
        TagListView.as_view()
    )
]
