"""ViewSets for Finances App."""

from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema_view

from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from apps.users.permissions import IsAdministrator
from .models import Revenue
from .serializers import RevenueReadSerializer, RevenueWriteSerializer
from .filters import RevenueFilter
from .schemas import revenue_schemas


@extend_schema_view(**revenue_schemas)
class RevenueViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for Revenue model.

    Endpoints:
    - GET /api/v1/revenues/
    - POST /api/v1/revenues/
    - GET /api/v1/revenues/{id}/
    - PUT /api/v1/revenues/{id}/
    - PATCH /api/v1/revenues/{id}/
    - DELETE /api/v1/revenues/{id}/
    """

    permission_classes = [IsAdministrator]
    serializer_class = RevenueWriteSerializer
    search_fields = ["order_id", "driver_id", "restaurant_id"]
    filterset_class = RevenueFilter

    def get_queryset(self):
        return Revenue.objects.get_available().select_related(
            "order_id", "driver_id", "restaurant_id"
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return RevenueReadSerializer
        return super().get_serializer_class()
