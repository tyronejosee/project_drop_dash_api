"""Views for Blogs App."""

from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from apps.users.permissions import IsAdministrator
from .models import Post, Tag
from .serializers import (
    PostWriteSerializer, PostReadSerializer, TagReadSerializer)


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
            return [IsAdministrator()]
        return super().get_permissions()

    def get(self, request):
        # Get a list of posts
        posts_cache = cache.get(self.cache_key)

        if posts_cache is None:
            posts = Post.objects.get_available()
            if not posts.exists():
                return Response(
                    {"details": "No posts available."},
                    status=status.HTTP_404_NOT_FOUND
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
    permission_classes = [IsAdministrator]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return super().get_permissions()

    def get_object(self, post_id):
        # Get a post instance by id
        return get_object_or_404(Post, pk=post_id)

    def get(self, request, post_id):
        # Get details of a post
        post = self.get_object(post_id)
        serializer = PostReadSerializer(post)
        return Response(serializer.data)

    @transaction.atomic
    def patch(self, request, post_id):
        # Partial update a post
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
        post.available = False  # Logical deletion
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FeaturedPostsView(APIView):
    """
    View to list featured posts.

    Endpoints:
    - GET api/v1/posts/featured/
    """
    cache_key = "featured_posts"

    def get(self, request):
        # Get a list of featured posts
        featured_posts_cache = cache.get(self.cache_key)

        if featured_posts_cache is None:
            featured_posts = Post.objects.get_featured()
            if not featured_posts.exists():
                return Response(
                    {"details": "No featured posts available."},
                    status=status.HTTP_404_NOT_FOUND
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
        # Get a list of recent posts (7 days)
        recent_posts_cache = cache.get(self.cache_key)

        if recent_posts_cache is None:
            recent_posts = Post.objects.get_recent()
            if not recent_posts.exists():
                return Response(
                    {"details": "No recent posts available."},
                    status=status.HTTP_404_NOT_FOUND
                )
            cache.set(self.cache_key, recent_posts, 7200)  # Set cache
            serializer = PostReadSerializer(recent_posts, many=True)
            return Response(serializer.data)

        serializer = PostReadSerializer(recent_posts_cache, many=True)
        return Response(serializer.data)


class TagListView(APIView):
    """Pending."""

    def get(self, request):
        #
        tags = Tag.objects.filter(available=True)
        if tags.exists():
            serializer = TagReadSerializer(tags, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No tags available."},
            status=status.HTTP_404_NOT_FOUND
        )
