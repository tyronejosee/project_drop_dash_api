"""Views for Coupons App."""

from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.utilities.pagination import MediumSetPagination
from .models import FixedCoupon, PercentageCoupon
from .serializers import FixedCouponSerializer, PercentageCouponSerializer
from .schemas import (
    fixed_coupon_list_schema,
    fixed_coupon_detail_schema,
    percentage_coupon_list_schema,
    percentage_coupon_detail_schema,
)


@extend_schema_view(**fixed_coupon_list_schema)
class FixedCouponListView(APIView):
    """View for listing and creating fixed coupons."""

    permission_classes = [IsAuthenticated]
    serializer_class = FixedCouponSerializer
    cache_key = "fixed_coupon_list"

    def get(self, request, format=None):
        # Get a list of available fixed coupons
        paginator = MediumSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            coupons = FixedCoupon.objects.get_all()
            if not coupons.exists():
                return Response(
                    {"detail": "No fixed coupons available."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            # Fetches the data from the database and serializes it
            paginated_data = paginator.paginate_queryset(coupons, request)
            serializer = self.serializer_class(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, 7200)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(cached_data, request)
            serializer = self.serializer_class(paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request, format=None):
        # Create a new fixed coupon
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**fixed_coupon_detail_schema)
class FixedCouponDetailView(APIView):
    """View to retrieve, update, and delete a fixed coupon."""

    permission_classes = [IsAuthenticated]
    serializer_class = FixedCouponSerializer

    def get_object(self, fixed_coupon_id):
        # Get a fixed coupon instance by id
        return get_object_or_404(FixedCoupon, pk=fixed_coupon_id)

    def get(self, request, fixed_coupon_id):
        # Get details of a fixed coupon
        fixed_coupon = self.get_object(fixed_coupon_id)
        serializer = self.serializer_class(fixed_coupon)
        return Response(serializer.data)

    @transaction.atomic
    def put(self, request, fixed_coupon_id):
        # Update a fixed coupon
        fixed_coupon = self.get_object(fixed_coupon_id)
        serializer = self.serializer_class(fixed_coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, fixed_coupon_id):
        # Delete a fixed coupon
        fixed_coupon = self.get_object(fixed_coupon_id)
        fixed_coupon.available = False  # Logical deletion
        fixed_coupon.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(**percentage_coupon_list_schema)
class PercentageCouponListView(APIView):
    """View for listing and creating percentage coupons."""

    permission_classes = [IsAuthenticated]
    serializer_class = PercentageCouponSerializer
    cache_key = "percentage_coupon"
    cache_timeout = 7200

    def get(self, request, format=None):
        # Get a list of available percentage coupons
        paginator = MediumSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            coupons = PercentageCoupon.objects.get_all()
            if not coupons.exists():
                return Response(
                    {"detail": "No percentage coupons available."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            paginated_data = paginator.paginate_queryset(coupons, request)
            serializer = self.serializer_class(paginated_data, many=True)
            # Set cache
            cache.set(self.cache_key, serializer.data, self.cache_timeout)
        else:
            # Retrieve the cached data and serialize it
            paginated_cached_data = paginator.paginate_queryset(cached_data, request)
            serializer = self.serializer_class(paginated_cached_data, many=True)

        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request, format=None):
        # Create a new percentage coupon
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache.delete(self.cache_key)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**percentage_coupon_detail_schema)
class PercentageCouponDetailView(APIView):
    """View to retrieve, update, and delete a percentage coupon."""

    permission_classes = [IsAuthenticated]
    serializer_class = PercentageCouponSerializer

    def get_object(self, percentage_coupon_id):
        # Get a percentage coupon instance by id
        return get_object_or_404(PercentageCoupon, pk=percentage_coupon_id)

    def get(self, request, percentage_coupon_id):
        # Get details of a percentage coupon
        percentage_coupon = self.get_object(percentage_coupon_id)
        serializer = self.serializer_class(percentage_coupon)
        return Response(serializer.data)

    @transaction.atomic
    def put(self, request, percentage_coupon_id):
        # Update a percentage coupon
        percentage_coupon = self.get_object(percentage_coupon_id)
        serializer = self.serializer_class(percentage_coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request, percentage_coupon_id):
        # Delete a percentage coupon
        percentage_coupon = self.get_object(percentage_coupon_id)
        percentage_coupon.available = False  # Logical deletion
        percentage_coupon.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckCouponView(APIView):
    """View to check the validity of a coupon code."""

    def get(self, request, format=None):
        """Handle GET requests to check the validity of a coupon code."""
        try:
            coupon_code = request.query_params.get("coupon_code")
            # coupon_code = request.data.get("coupon_code")

            fixed_coupon = FixedCoupon.objects.filter(code=coupon_code).first()
            percentage_coupon = PercentageCoupon.objects.filter(
                code=coupon_code
            ).first()

            if fixed_coupon:
                serializer = FixedCouponSerializer(fixed_coupon)
                return Response(serializer.data)
            elif percentage_coupon:
                serializer = PercentageCouponSerializer(percentage_coupon)
                return Response(serializer.data)
            else:
                return Response(
                    {"errors": "Coupon code not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        except Exception as e:
            return Response(
                {"errors": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
