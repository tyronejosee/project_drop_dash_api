"""URLs for Blogs App."""

from django.urls import path

from .views import PostListView, PostDetailView, TagListView


urlpatterns = [
    path(
        "api/v1/posts/",
        PostListView.as_view()
    ),
    path(
        "api/v1/posts/<uuid:post_id>/",
        PostDetailView.as_view()
    ),
    path(
        "api/v1/posts/tags/",
        TagListView.as_view()
    )
]
