"""ViewSets for Promotions App."""

from rest_framework.viewsets import ModelViewSet

from apps.users.permissions import IsMarketing
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Promotion, FixedCoupon, PercentageCoupon
from .serializers import (
    PromotionReadSerializer,
    PromotionWriteSerializer,
    FixedCouponReadSerializer,
    FixedCouponWriteSerializer,
    PercentageCouponReadSerializer,
    PercentageCouponWriteSerializer,
)


class PromotionViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Promotion instances.

    Endpoints:
    - GET /api/v1/promotions/
    - POST /api/v1/promotions/
    - GET /api/v1/promotions/{id}/
    - PUT /api/v1/promotions/{id}/
    - PATCH /api/v1/promotions/{id}/
    - DELETE /api/v1/promotions/{id}/
    """

    permission_classes = [IsMarketing]
    serializer_class = PromotionWriteSerializer
    search_fields = ["name"]
    # filterset_class = PromotionFilter

    def get_queryset(self):
        return Promotion.objects.get_active()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PromotionReadSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class FixedCoponViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing FixedCoupon instances.

    Endpoints:
    - GET /api/v1/fixed-coupon/
    - POST /api/v1/fixed-coupon/
    - GET /api/v1/fixed-coupon/{id}/
    - PUT /api/v1/fixed-coupon/{id}/
    - PATCH /api/v1/fixed-coupon/{id}/
    - DELETE /api/v1/fixed-coupon/{id}/
    """

    permission_classes = [IsMarketing]
    serializer_class = FixedCouponWriteSerializer
    search_fields = ["name"]
    # filterset_class = FixedCouponFilter

    def get_queryset(self):
        return FixedCoupon.objects.get_active()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FixedCouponReadSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class PercentageCoponViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing FixedCoupon instances.

    Endpoints:
    - GET /api/v1/percentage-coupons/
    - POST /api/v1/percentage-coupons/
    - GET /api/v1/percentage-coupons/{id}/
    - PUT /api/v1/percentage-coupons/{id}/
    - PATCH /api/v1/percentage-coupons/{id}/
    - DELETE /api/v1/percentage-coupons/{id}/
    """

    permission_classes = [IsMarketing]
    serializer_class = PercentageCouponWriteSerializer
    search_fields = ["name"]
    # filterset_class = FixedCouponFilter

    def get_queryset(self):
        return PercentageCoupon.objects.get_active()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PercentageCouponReadSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
