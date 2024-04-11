"""Views for Categories App."""

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.pagination import LargeSetPagination
from apps.utilities.permissions import IsStaffOrReadOnly
from .models import Category
from .serializers import CategorySerializer


class CategoryList(APIView):
    """APIView to list and create categories."""
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]

    def get(self, request):
        """Get a list of categories."""
        categories = Category.objects.filter(available=True).order_by("id")
        if categories.exists():
            paginator = LargeSetPagination()
            page = paginator.paginate_queryset(categories, request)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return paginator.get_paginated_response(serializer.data)
        return Response(
            {"details": "No categories available."},
            status=status.HTTP_204_NO_CONTENT
        )

    def post(self, request):
        """Create a new category."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class CategoryDetail(APIView):
    """APIView to retrieve, update, and delete a category."""
    serializer_class = CategorySerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_object(self, category_id):
        """Get a category instance by id."""
        try:
            return Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, category_id):
        """Get details of a category."""
        category = self.get_object(category_id)
        serializer = self.serializer_class(category)
        return Response(serializer.data)

    def put(self, request, category_id):
        """Update a category."""
        category = self.get_object(category_id)
        serializer = self.serializer_class(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.error,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, category_id):
        """Delete a category."""
        category = self.get_object(category_id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
