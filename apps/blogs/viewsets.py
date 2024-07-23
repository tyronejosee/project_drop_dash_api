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

from apps.users.permissions import IsMarketing, IsClient
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Post, PostReport
from .serializers import (
    PostReadSerializer,
    PostWriteSerializer,
    PostReportReadSerializer,
    PostReportWriteSerializer,
)
from .choices import PriorityChoices


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
            if PostReport.objects.filter(post_id=post, user_id=request.user).exists():
                return Response(
                    {"detail": "You have already reported this post."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            with transaction.atomic():
                # Update points of the post
                post.points = post.points - 1
                if post.points <= 5:
                    post.is_available = False
                post.save()

                # Determine priority for the new report
                if post.points <= 25:
                    priority = PriorityChoices.URGENT
                elif post.points <= 50:
                    priority = PriorityChoices.HIGH
                elif post.points <= 75:
                    priority = PriorityChoices.MEDIUM
                else:
                    priority = PriorityChoices.LOW

                serializer.save(user_id=request.user, post_id=post, priority=priority)
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
