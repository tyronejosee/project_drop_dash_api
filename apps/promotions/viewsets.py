"""ViewSets for Promotions App."""

from rest_framework.viewsets import ModelViewSet

from apps.users.permissions import IsMarketing
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Promotion
from .serializers import PromotionReadSerializer, PromotionWriteSerializer


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
        return Promotion.objects.get_available()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return PromotionReadSerializer
        return super().get_serializer_class()
