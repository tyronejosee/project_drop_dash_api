"""Views for Categories App."""

from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsAdministrator, IsBusiness
from apps.utilities.pagination import LargeSetPagination
from .models import Category
from .serializers import CategorySerializer


class CategoryList(APIView):
    """APIView to list and create categories."""
    permission_classes = [IsAdministrator]
    serializer_class = CategorySerializer
    cache_key = "category_list"
    cache_timeout = 7200  # 2 hours

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsBusiness()]
        return super().get_permissions()

    def get(self, request, format=None):
        # Get a list of categories
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            categories = Category.objects.get_all()
            # TODO: Fix query only restaurant
            if not categories.exists():
                return Response(
                    {"details": "No categories available."},
                    status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(categories, request)
            serializer = self.serializer_class(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, self.cache_timeout)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(
                cached_data, request)
            serializer = self.serializer_class(
                paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        # Create a new category
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """APIView to retrieve, update, and delete a category."""
    permission_classes = [IsBusiness]
    serializer_class = CategorySerializer

    def get_object(self, category_id):
        # Get a category instance by id
        return get_object_or_404(Category, pk=category_id)

    def get(self, request, category_id, format=None):
        # Get details of a category
        category = self.get_object(category_id)
        serializer = self.serializer_class(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, category_id, format=None):
        # Update a category
        category = self.get_object(category_id)
        serializer = self.serializer_class(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id, format=None):
        # Delete a category
        category = self.get_object(category_id)
        category.available = False  # Logical deletion
        category.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
