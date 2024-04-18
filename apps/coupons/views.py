"""Views for Coupons App."""

from django.db import transaction
from django.core.cache import cache
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
    """Pending."""
    permission_classes = [IsAuthenticated]
    serializer_class = FixedCouponSerializer
    pagination_class = MediumSetPagination
    CACHE_TIMEOUT = 7200  # Cache for 2 hours

    def get(self, request, format=None):
        # Pending
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
        # Pending
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
