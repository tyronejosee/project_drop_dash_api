"""Views for Blogs App."""

from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.pagination import MediumSetPagination
from apps.utilities.permissions import IsStaffOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostListView(APIView):
    """View to list and create posts."""
    permission_classes = [IsStaffOrReadOnly]
    cache_key = "post_list"
    cache_timeout = 7200  # 2 hours

    def get(self, request, format=None):
        # Get a list of posts
        paginator = MediumSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            posts = Post.objects.filter(available=True)
            if not posts.exists():
                return Response(
                    {"details": "No posts available."},
                    status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(posts, request)
            serializer = PostSerializer(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, self.cache_timeout)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(
                cached_data, request)
            serializer = PostSerializer(paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        # Create a new post
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
