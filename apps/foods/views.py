"""Views for Foods App."""

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.pagination import MediumSetPagination
from .models import Food
from .serializers import FoodSerializer


class FoodList(APIView):
    """APIView to list and create foods."""
    serializer_class = FoodSerializer
    # permission_classes = # TODO: Add permission for restaurant

    def get(self, request, format=None):
        """Get a list of foods."""
        foods = Food.objects.filter(available=True).order_by("id")
        if foods.exists():
            paginator = MediumSetPagination()
            page = paginator.paginate_queryset(foods, request)
            if page is not None:
                serializer = self.serializer_class(page, many=True)
                return paginator.get_paginated_response(serializer.data)

        return Response(
            {"details": "No Foods Available."},
            status=status.HTTP_204_NO_CONTENT
        )

    def post(self, request, format=None):
        """Create a new food."""
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


class FoodDetail(APIView):
    """APIView to retrieve, update, and delete a food."""
    serializer_class = FoodSerializer
    # permission_classes = # TODO: Add permission for restaurant

    def get_object(self, food_id):
        """Get a food instance by id."""
        try:
            return Food.objects.get(pk=food_id)
        except Food.DoesNotExist:
            raise Http404

    def get(self, request, food_id, format=None):
        """Get details of a food."""
        food = self.get_object(food_id)
        serializer = self.serializer_class(food)
        return Response(serializer.data)

    def put(self, request, food_id, format=None):
        """Update a food."""
        food = self.get_object(food_id)
        serializer = self.serializer_class(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.error,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, food_id, format=None):
        """Delete a food."""
        food = self.get_object(food_id)
        food.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
