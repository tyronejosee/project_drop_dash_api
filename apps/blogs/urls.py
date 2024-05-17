"""URLs for Blogs App."""

from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostSearchView,
    FeaturedPostsView,
    RecentPostsView,
    TagListView,
    PostReportView
)


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
        "api/v1/posts/<uuid:post_id>/report/",
        PostReportView.as_view()
    ),
    path(
        "api/v1/posts/search/",
        PostSearchView.as_view()
    ),
    path(
        "api/v1/posts/featured/",
        FeaturedPostsView.as_view()
    ),
    path(
        "api/v1/posts/recent/",
        RecentPostsView.as_view()
    ),
    path(
        "api/v1/posts/tags/",
        TagListView.as_view()
    ),

]
