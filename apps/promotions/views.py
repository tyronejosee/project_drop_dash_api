"""Views for Promotions App."""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsMarketing
from .models import FixedCoupon, PercentageCoupon
from .serializers import FixedCouponReadSerializer, PercentageCouponReadSerializer


class CheckCouponView(APIView):
    """
    View to check the validity of a coupon code.

    Endpoints:
    - GET api/v1/coupons/check/?coupon_code={id}
    """

    permission_classes = [IsMarketing]

    def get(self, request, format=None):
        # Check the validity of a coupon code
        try:
            code = request.query_params.get("coupon_code", None)
            if not code:
                return Response(
                    {"detail": "Coupon code is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            fixed_coupon = FixedCoupon.objects.get_by_code(code)
            percentage_coupon = PercentageCoupon.objects.get_by_code(code)

            if fixed_coupon:
                serializer = FixedCouponReadSerializer(fixed_coupon)
                return Response(serializer.data)
            elif percentage_coupon:
                serializer = PercentageCouponReadSerializer(percentage_coupon)
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
