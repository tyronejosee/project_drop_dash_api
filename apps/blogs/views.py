"""Views for Blogs App."""

import re
from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from apps.users.permissions import IsSupport, IsClient
from .models import Post, Tag, PostReport
from .serializers import (
    PostWriteSerializer,
    PostReadSerializer,
    TagWriteSerializer,
    TagReadSerializer,
    PostReportWriteSerializer,
)
from .choices import Priority


class TagListView(APIView):
    """
    View to list and create tags.

    Endpoints:
    - GET api/v1/posts/tags/
    - POST api/v1/posts/tags/
    """

    permission_classes = [IsSupport]
    cache_key = "promotion_list"

    def get(self, request):
        # Get all tags
        tags = Tag.objects.get_available()
        if tags.exists():
            serializer = TagReadSerializer(tags, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No tags available."}, status=status.HTTP_404_NOT_FOUND
        )

    def post(self, request):
        # Create a new tag
        serializer = TagWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostListView(APIView):
    """
    View to list and create posts.

    Endpoints:
    - GET api/v1/posts/
    - POST api/v1/posts/
    """

    cache_key = "post_list"

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsSupport()]
        return super().get_permissions()

    def get(self, request):
        # Get all posts
        posts_cache = cache.get(self.cache_key)

        if posts_cache is None:
            posts = Post.objects.get_available()
            if not posts.exists():
                return Response(
                    {"detail": "No posts available."}, status=status.HTTP_404_NOT_FOUND
                )
            cache.set(self.cache_key, posts, 7200)  # Set cache
            serializer = PostReadSerializer(posts, many=True)
            return Response(serializer.data)

        serializer = PostReadSerializer(posts_cache, many=True)
        return Response(serializer.data)

    @transaction.atomic
    def post(self, request):
        # Create a new post
        serializer = PostWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            cache.delete(self.cache_key)  # Invalidate cache
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetailView(APIView):
    """
    View to retrieve, update, and delete a post.

    Endpoints:
    - GET api/v1/posts/{id}/
    - PATCH api/v1/posts/{id}/
    - DELETE api/v1/posts/{id}/
    """

    permission_classes = [IsSupport]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return super().get_permissions()

    def get_object(self, post_id):
        return get_object_or_404(Post, pk=post_id)

    def get(self, request, post_id):
        # Get a post
        post = self.get_object(post_id)
        serializer = PostReadSerializer(post)
        return Response(serializer.data)

    @transaction.atomic
    def patch(self, request, post_id):
        # Update a post (Partial)
        post = self.get_object(post_id)
        serializer = PostWriteSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, post_id):
        # Delete a post
        post = self.get_object(post_id)
        if post.author != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.available = False  # Logical deletion
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostSearchView(APIView):
    """
    View to search posts.

    Endpoints:
    - GET api/v1/posts/?q={query}
    """

    def get(self, request):
        # Search posts for title, content and tag fields
        search_term = request.query_params.get("q", "")
        search_term = re.sub(r"[^\w\s\-\(\)\.,]", "", search_term).strip()
        print(search_term)

        if not search_term:
            return Response(
                {"detail": "No search query provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        posts = Post.objects.get_search(search_term)

        if not posts.exists():
            return Response(
                {"detail": "No results found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PostReadSerializer(posts, many=True)
        return Response(serializer.data)


class FeaturedPostsView(APIView):
    """
    View to list featured posts.

    Endpoints:
    - GET api/v1/posts/featured/
    """

    cache_key = "featured_posts"

    def get(self, request):
        # Get all featured posts
        featured_posts_cache = cache.get(self.cache_key)

        if featured_posts_cache is None:
            featured_posts = Post.objects.get_featured()
            if not featured_posts.exists():
                return Response(
                    {"detail": "No featured posts available."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            cache.set(self.cache_key, featured_posts, 7200)  # Set cache
            serializer = PostReadSerializer(featured_posts, many=True)
            return Response(serializer.data)

        serializer = PostReadSerializer(featured_posts_cache, many=True)
        return Response(serializer.data)


class RecentPostsView(APIView):
    """
    View to list recent posts.

    Endpoints:
    - GET api/v1/posts/recent/
    """

    cache_key = "recent_posts"

    def get(self, request):
        # Get all recent posts (7 days)
        recent_posts_cache = cache.get(self.cache_key)

        if recent_posts_cache is None:
            recent_posts = Post.objects.get_recent()
            if not recent_posts.exists():
                return Response(
                    {"detail": "No recent posts available."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            cache.set(self.cache_key, recent_posts, 7200)  # Set cache
            serializer = PostReadSerializer(recent_posts, many=True)
            return Response(serializer.data)

        serializer = PostReadSerializer(recent_posts_cache, many=True)
        return Response(serializer.data)


class PostReportView(APIView):
    """
    View for reporting a post.

    Endpoints:
    - POST api/v1/posts/{id}/report/
    """

    permission_classes = [IsClient]

    def post(self, request, post_id):
        serializer = PostReportWriteSerializer(data=request.data)
        if serializer.is_valid():
            post = get_object_or_404(Post, pk=post_id)

            # Check if the user has already reported this post
            if PostReport.objects.filter(post=post, user=request.user).exists():
                return Response(
                    {"detail": "You have already reported this post."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            with transaction.atomic():
                # Update points of the post
                post.points = post.points - 1
                if post.points <= 5:
                    post.available = False
                post.save()

                # Determine priority for the new report
                if post.points <= 25:
                    priority = Priority.URGENT
                elif post.points <= 50:
                    priority = Priority.HIGH
                elif post.points <= 75:
                    priority = Priority.MEDIUM
                else:
                    priority = Priority.LOW

                serializer.save(user=request.user, post=post, priority=priority)
            return Response(
                {"detail": "Your report has been submitted successfully."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
