"""Views for Coupons App."""


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import FixedDiscountCoupon, PercentageDiscountCoupon
from .serializers import (
    FixedDiscountCouponSerializer, PercentageDiscountCouponSerializer
)


class CheckCouponAPIView(APIView):
    """APIView to check the validity of a coupon code."""

    def get(self, request, format=None):
        """Handle GET requests to check the validity of a coupon code."""
        try:
            coupon_code = request.query_params.get("coupon_code")
            # coupon_code = request.data.get("coupon_code")

            fixed_coupon = FixedDiscountCoupon.objects.filter(
                code=coupon_code).first()
            percentage_coupon = PercentageDiscountCoupon.objects.filter(
                code=coupon_code).first()

            if fixed_coupon:
                serializer = FixedDiscountCouponSerializer(fixed_coupon)
                return Response(serializer.data)
            elif percentage_coupon:
                serializer = PercentageDiscountCouponSerializer(
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
