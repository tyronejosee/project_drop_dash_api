"""Views for Promotions App."""

import re
from django.db import transaction
from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsMarketing
from apps.utilities.pagination import LargeSetPagination
from .models import Promotion, FixedCoupon, PercentageCoupon
from .serializers import (
    PromotionReadSerializer,
    PromotionWriteSerializer,
    FixedCouponReadSerializer,
    FixedCouponWriteSerializer,
    PercentageCouponReadSerializer,
    PercentageCouponWriteSerializer,
)
from .schemas import (
    promotion_list_schema,
    promotion_detail_schema,
    fixed_coupon_list_schema,
    fixed_coupon_detail_schema,
    percentage_coupon_list_schema,
    percentage_coupon_detail_schema,
)


@extend_schema_view(**promotion_list_schema)
class PromotionListView(APIView):
    """
    View to list and create promotions.

    Endpoints:
    - GET api/v1/promotions/
    - POST api/v1/promotions/
    """

    permission_classes = [IsMarketing]
    cache_key = "promotion_list"

    def get(self, request):
        # Get a list of promotions
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            promotions = Promotion.objects.get_available()
            if not promotions.exists():
                return Response(
                    {"detail": "No promotions available."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            page = paginator.paginate_queryset(promotions, request)
            serializer = PromotionReadSerializer(page, many=True)
            cache.set(self.cache_key, serializer.data, 7200)  # 2 hrs.
            return paginator.get_paginated_response(serializer.data)

        page = paginator.paginate_queryset(cached_data, request)
        serializer = PromotionReadSerializer(page, many=True)
        return paginator.get_paginated_response(cached_data)

    @transaction.atomic
    def post(self, request):
        # Create a promotion
        serializer = PromotionWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            cache.delete(self.cache_key)  # Invalidate cache
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**promotion_detail_schema)
class PromotionDetailView(APIView):
    """
    View to update and delete a promotion.

    Endpoints:
    - PATCH api/v1/promotions/{id}/
    - DELETE api/v1/promotions/{id}/
    """

    permission_classes = [IsMarketing]
    cache_key = "promotion_list"

    def get_object(self, promotion_id):
        # Get a promotion instance by id
        return get_object_or_404(Promotion, pk=promotion_id)

    @transaction.atomic
    def patch(self, request, promotion_id):
        # Update a promotion
        promotion = self.get_object(promotion_id)

        if promotion.creator == request.user:
            serializer = PromotionWriteSerializer(
                promotion, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"detail": "You are not the owner of this promotion."},
            status=status.HTTP_403_FORBIDDEN,
        )

    @transaction.atomic
    def delete(self, request, promotion_id):
        # Delete a promotion
        promotion = self.get_object(promotion_id)
        promotion.is_available = False
        cache.delete(self.cache_key)
        promotion.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PromotionSearchView(APIView):
    """
    View to search promotions.

    Endpoints:
    - GET api/v1/promotions/?q={query}
    """

    def get(self, request):
        # Search for promotions for name and conditions fields
        search_term = request.query_params.get("q", "")
        search_term = re.sub(r"[^\w\s\-\(\)\.,]", "", search_term).strip()

        if not search_term:
            return Response(
                {"detail": "No search query provided"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        promotions = Promotion.objects.get_search(search_term)

        if not promotions.exists():
            return Response(
                {"detail": "No results found."}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PromotionReadSerializer(promotions, many=True)
        return Response(serializer.data)


@extend_schema_view(**fixed_coupon_list_schema)
class FixedCouponListView(APIView):
    """
    View for listing and creating fixed coupons.

    Endpoints:
    - GET api/v1/coupons/fixed/
    - POST api/v1/coupons/fixed/
    """

    permission_classes = [IsMarketing]
    cache_key = "fixed_coupon_list"

    def get(self, request, format=None):
        # Get a list of available fixed coupons
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            coupons = FixedCoupon.objects.get_available()
            if not coupons.exists():
                return Response(
                    {"detail": "No fixed coupons available."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            paginated_data = paginator.paginate_queryset(coupons, request)
            serializer = FixedCouponReadSerializer(paginated_data, many=True)
            cache.set(self.cache_key, serializer.data, 7200)
            return paginator.get_paginated_response(serializer.data)

        paginated_cached_data = paginator.paginate_queryset(cached_data, request)
        serializer = FixedCouponReadSerializer(paginated_cached_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request, format=None):
        # Create a new fixed coupon
        serializer = FixedCouponWriteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(creator=request.user)
            cache.delete(self.cache_key)  # Invalidate cache
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**fixed_coupon_detail_schema)
class FixedCouponDetailView(APIView):
    """
    View to update, and delete a fixed coupon.

    Endpoints:
    - PATCH api/v1/coupons/fixed/{id}/
    - DELETE api/v1/coupons/fixed/{id}/
    """

    permission_classes = [IsMarketing]
    cache_key = "fixed_coupon_list"

    def get_object(self, fixed_coupon_id):
        # Get a fixed coupon instance by id
        return get_object_or_404(FixedCoupon, pk=fixed_coupon_id)

    @transaction.atomic
    def patch(self, request, fixed_coupon_id):
        # Update a promotion
        fixed_coupon = self.get_object(fixed_coupon_id)

        if fixed_coupon.creator == request.user:
            serializer = FixedCouponWriteSerializer(
                fixed_coupon, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            {"detail": "You are not the owner of this coupon."},
            status=status.HTTP_403_FORBIDDEN,
        )

    @transaction.atomic
    def delete(self, request, fixed_coupon_id):
        # Delete a fixed coupon
        fixed_coupon = self.get_object(fixed_coupon_id)
        fixed_coupon.is_available = False
        cache.delete(self.cache_key)
        fixed_coupon.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema_view(**percentage_coupon_list_schema)
class PercentageCouponListView(APIView):
    """
    View for listing and creating percentage coupons.

    Endpoints:
    - GET api/v1/coupons/percentage/
    - POST api/v1/coupons/percentage/
    """

    permission_classes = [IsMarketing]
    cache_key = "percentage_coupon_list"

    def get(self, request, format=None):
        # Get a list of available percentage coupons
        paginator = LargeSetPagination()
        cached_data = cache.get(self.cache_key)

        if cached_data is None:
            coupons = PercentageCoupon.objects.get_available()
            if not coupons.exists():
                return Response(
                    {"detail": "No percentage coupons available."},
                    status=status.HTTP_404_NOT_FOUND,
                )

            paginated_data = paginator.paginate_queryset(coupons, request)
            serializer = PercentageCouponReadSerializer(paginated_data, many=True)
            cache.set(self.cache_key, serializer.data, 7200)  # 2 hrs.
            return paginator.get_paginated_response(serializer.data)

        paginated_cached_data = paginator.paginate_queryset(cached_data, request)
        serializer = PercentageCouponReadSerializer(paginated_cached_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    @transaction.atomic
    def post(self, request, format=None):
        # Create a new percentage coupon
        serializer = PercentageCouponWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            cache.delete(self.cache_key)  # Invalidate cache
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema_view(**percentage_coupon_detail_schema)
class PercentageCouponDetailView(APIView):
    """
    View to update, and delete a percentage coupon.

    Endpoints:
    - PATCH api/v1/coupons/percentage/{id}/
    - DELETE api/v1/coupons/percentage/{id}/
    """

    permission_classes = [IsMarketing]
    cache_key = "percentage_coupon_list"

    def get_object(self, percentage_coupon_id):
        # Get a percentage coupon instance by id
        return get_object_or_404(PercentageCoupon, pk=percentage_coupon_id)

    @transaction.atomic
    def patch(self, request, percentage_coupon_id):
        # Update a percentage coupon
        percentage_coupon = self.get_object(percentage_coupon_id)

        if percentage_coupon.creator == request.user:
            serializer = PercentageCouponWriteSerializer(
                percentage_coupon, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"detail": "You are not the owner of this coupon."},
            status=status.HTTP_403_FORBIDDEN,
        )

    @transaction.atomic
    def delete(self, request, percentage_coupon_id):
        # Delete a percentage coupon
        percentage_coupon = self.get_object(percentage_coupon_id)
        percentage_coupon.is_available = False
        cache.delete(self.cache_key)
        percentage_coupon.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
