"""ViewSets for Blogs App."""

from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsMarketing, IsClient
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Post, PostReport, Tag
from .services import PostService
from .serializers import (
    PostReadSerializer,
    PostWriteSerializer,
    PostReportReadSerializer,
    PostReportWriteSerializer,
    TagReadSerializer,
    TagWriteSerializer,
)
from .schemas import post_schemas


@extend_schema_view(**post_schemas)
class PostViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Country instances.

    Endpoints:
    - GET /api/v1/posts/
    - POST /api/v1/posts/
    - GET /api/v1/posts/{id}/
    - PUT /api/v1/posts/{id}/
    - PATCH /api/v1/posts/{id}/
    - DELETE /api/v1/posts/{id}/
    """

    permission_classes = [IsMarketing]
    serializer_class = PostWriteSerializer
    search_fields = ["title"]
    # filterset_class = PostFilter

    def get_queryset(self):
        return (
            Post.objects.get_available()
            .select_related("author_id")
            .prefetch_related("tags")
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PostReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsClient],
        url_path="report",
    )
    def create_report(self, request, *args, **kwargs):
        """
        Action report a specific post by ID.

        Endpoints:
        - GET api/v1/posts/{id}/report/
        """
        post = self.get_object()
        serializer = PostReportWriteSerializer(data=request.data)
        if serializer.is_valid():
            try:
                PostService.validate_report(post, request.user)
            except Exception as e:
                return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

            with transaction.atomic():
                PostService.update_post_points(post)
                PostService.create_report(serializer, post, request.user)

            return Response(
                {"detail": "Your report has been submitted successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsMarketing],
        url_path="reports",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_reports(self, request, *args, **kwargs):
        """
        Action retrieve a list of all post reports.

        Endpoints:
        - GET api/v1/posts/reports/
        """
        reports = PostReport.objects.get_available()
        if reports.exists():
            serializer = PostReportReadSerializer(reports, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No reports found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="featured",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_featured_posts(self, request, *args, **kwargs):
        """
        Action retrieve all featured posts.

        Endpoints:
        - GET api/v1/posts/featured/
        """
        featured_posts = Post.objects.get_featured()
        if featured_posts.exists():
            serializer = PostReadSerializer(featured_posts, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No featured posts found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="recent",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_recent_posts(self, request, *args, **kwargs):
        """
        Action retrieve all recent posts (7 days).

        Endpoints:
        - GET api/v1/posts/recent/
        """
        recent_posts = Post.objects.get_recent()
        if recent_posts.exists():
            serializer = PostReadSerializer(recent_posts, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No recent posts found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],
        url_path="tags",
    )
    @method_decorator(cache_page(60 * 60 * 2))
    @method_decorator(vary_on_headers("User-Agent"))
    def get_tags(self, request, *args, **kwargs):
        """
        Action retrieve all tags.

        Endpoints:
        - GET api/v1/posts/tags/
        """
        tags = Tag.objects.get_available()
        if tags.exists():
            serializer = TagReadSerializer(tags, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No tags found."},
            status=status.HTTP_404_NOT_FOUND,
        )

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[IsMarketing],
        url_path="create-tag",
    )
    def create_tag(self, request, *args, **kwargs):
        """
        Action create a new tag.

        Endpoints:
        - POST api/v1/posts/create-tag/
        """
        serializer = TagWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
