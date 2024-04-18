"""Views for Coupons App."""

from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from apps.utilities.pagination import MediumSetPagination
from .models import FixedCoupon, PercentageCoupon
from .serializers import (
    FixedCouponSerializer, PercentageCouponSerializer
)


class FixedCouponListAPIView(APIView):
    """APIView for listing and creating fixed coupons."""
    permission_classes = [IsAuthenticated]
    serializer_class = FixedCouponSerializer
    pagination_class = MediumSetPagination
    CACHE_TIMEOUT = 7200  # Cache for 2 hours

    def get(self, request, format=None):
        # Get a list of available fixed coupons
        cache_key = f"fixed_coupon_{request.user.id}"
        cached_data = cache.get(cache_key)

        if cached_data is None:
            coupons = FixedCoupon.objects.filter(available=True).order_by("id")
            if coupons.exists():
                serializer = self.serializer_class(coupons, many=True)
                # Set cache
                cache.set(cache_key, serializer.data, self.CACHE_TIMEOUT)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"detail": "No fixed coupons available."},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(cached_data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request, format=None):
        # Create a new fixed coupon
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache_key = f"fixed_coupon_{request.user.id}"
            cache.delete(cache_key)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class FixedCouponDetailAPIView(APIView):
    """APIView to retrieve, update, and delete a fixed coupon."""
    permission_classes = [IsAuthenticated]
    serializer_class = FixedCouponSerializer

    def get_object(self, fixed_coupon_id):
        # Get a fixed coupon instance by id
        return get_object_or_404(FixedCoupon, pk=fixed_coupon_id)

    def get(self, request, fixed_coupon_id):
        # Get details of a fixed coupon
        fixed_coupon = self.get_object(fixed_coupon_id)
        serializer = self.serializer_class(fixed_coupon)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def put(self, request, fixed_coupon_id):
        # Update a fixed coupon
        fixed_coupon = self.get_object(fixed_coupon_id)
        serializer = self.serializer_class(fixed_coupon, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @transaction.atomic
    def delete(self, request, fixed_coupon_id):
        # Delete a fixed coupon
        fixed_coupon = self.get_object(fixed_coupon_id)
        fixed_coupon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PercentageCouponListAPIView(APIView):
    """APIView for listing and creating percentage coupons."""
    permission_classes = [IsAuthenticated]
    serializer_class = PercentageCouponSerializer
    pagination_class = MediumSetPagination
    CACHE_TIMEOUT = 7200  # Cache for 2 hours

    def get(self, request, format=None):
        # Get a list of available percentage coupons
        cache_key = f"percentage_coupon_{request.user.id}"
        cached_data = cache.get(cache_key)

        if cached_data is None:
            coupons = PercentageCoupon.objects.filter(
                available=True).order_by("id")
            if coupons.exists():
                serializer = self.serializer_class(coupons, many=True)
                # Set cache
                cache.set(cache_key, serializer.data, self.CACHE_TIMEOUT)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"detail": "No percentage coupons available."},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(cached_data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request, format=None):
        # Create a new percentage coupon
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Invalidate cache
            cache_key = f"percentage_coupon_{request.user.id}"
            cache.delete(cache_key)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class PercentageCouponDetailAPIView(APIView):
    """APIView to retrieve, update, and delete a percentage coupon."""
    permission_classes = [IsAuthenticated]
    serializer_class = PercentageCouponSerializer

    def get_object(self, percentage_coupon_id):
        # Get a percentage coupon instance by id
        return get_object_or_404(PercentageCoupon, pk=percentage_coupon_id)

    def get(self, request, percentage_coupon_id):
        # Get details of a percentage coupon
        percentage_coupon = self.get_object(percentage_coupon_id)
        serializer = self.serializer_class(percentage_coupon)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def put(self, request, percentage_coupon_id):
        # Update a percentage coupon
        percentage_coupon = self.get_object(percentage_coupon_id)
        serializer = self.serializer_class(
            percentage_coupon, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @transaction.atomic
    def delete(self, request, percentage_coupon_id):
        # Delete a percentage coupon
        percentage_coupon = self.get_object(percentage_coupon_id)
        percentage_coupon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CheckCouponAPIView(APIView):
    """APIView to check the validity of a coupon code."""

    def get(self, request, format=None):
        """Handle GET requests to check the validity of a coupon code."""
        try:
            coupon_code = request.query_params.get("coupon_code")
            # coupon_code = request.data.get("coupon_code")

            fixed_coupon = FixedCoupon.objects.filter(
                code=coupon_code).first()
            percentage_coupon = PercentageCoupon.objects.filter(
                code=coupon_code).first()

            if fixed_coupon:
                serializer = FixedCouponSerializer(fixed_coupon)
                return Response(serializer.data)
            elif percentage_coupon:
                serializer = PercentageCouponSerializer(
                    percentage_coupon)
                return Response(serializer.data)
            else:
                return Response(
                    {"errors": "Coupon code not found"},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                {"errors": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
