"""Views for Blogs App."""

from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsAdministrator
from .models import Post, Tag
from .serializers import PostWriteSerializer, PostReadSerializer, TagReadSerializer


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

    def get(self, request, format=None):
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

    def post(self, request, format=None):
        # Create a new post
        serializer = PostWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            cache.delete(self.cache_key)  # Invalidate cache
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagListView(APIView):
    """Pending."""

    def get(self, request, format=None):
        #
        tags = Tag.objects.filter(available=True)
        if tags.exists():
            serializer = TagReadSerializer(tags, many=True)
            return Response(serializer.data)
        return Response(
            {"detail": "No tags available."},
            status=status.HTTP_404_NOT_FOUND
        )
