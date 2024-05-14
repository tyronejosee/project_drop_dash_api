"""Views for Promotions App."""

from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsAdministrator
from apps.utilities.pagination import MediumSetPagination
from .models import Promotion
from .serializers import PromotionReadSerializer, PromotionWriteSerializer
from .schemas import promotion_list_schema, promotion_detail_schema


@extend_schema_view(**promotion_list_schema)
class PromotionListView(APIView):
    """
    View to list and create promotions.

    Endpoints:
    - GET api/v1/promotions/
    - POST api/v1/promotions/
    """
    permission_classes = [IsAdministrator]
    cache_key = "promotion_list"

    def get(self, request):
        # Get a list of promotions
        paginator = MediumSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            promotions = Promotion.objects.get_available()
            if not promotions.exists():
                return Response(
                    {"detail": "No promotions available."},
                    status=status.HTTP_404_NOT_FOUND
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(promotions, request)
            cache.set(self.cache_key, paginated_data, 7200)  # 2 hrs.
            serializer = PromotionReadSerializer(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(
                cached_data, request)
            serializer = PromotionReadSerializer(
                paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request):
        # Create a new promotion
        serializer = PromotionWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            cache.delete(self.cache_key)  # Invalidate cache
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**promotion_detail_schema)
class PromotionDetailView(APIView):
    """View to retrieve and delete a promotion."""
    permission_classes = [IsAdministrator]

    def get_object(self, promotion_id):
        # Get a promotion instance by id
        return get_object_or_404(Promotion, pk=promotion_id)

    def get(self, request, promotion_id):
        # Get details of a promotion
        promotion = self.get_object(promotion_id)
        serializer = PromotionReadSerializer(promotion)
        return Response(serializer.data)

    @transaction.atomic
    def delete(self, request, promotion_id):
        # Delete a promotion
        promotion = self.get_object(promotion_id)
        promotion.available = False  # Logical deletion
        promotion.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
