"""ViewSets for Home App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from apps.users.permissions import IsMarketing
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Page, Keyword
from .serializers import (
    PageReadSerializer,
    PageWriteSerializer,
    PageMinimalSerializer,
    KeywordReadSerializer,
    KeywordWriteSerializer,
)


class PageViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Page instances.

    Endpoints:
    - GET /api/v1/pages/
    - POST /api/v1/pages/
    - GET /api/v1/pages/{id}/
    - PUT /api/v1/pages/{id}/
    - PATCH /api/v1/pages/{id}/
    - DELETE /api/v1/pages/{id}/
    """

    permission_classes = [IsMarketing]
    serializer_class = PageWriteSerializer
    search_fields = ["name"]

    def get_queryset(self):
        if self.action == "list":
            return Page.objects.get_available().only("id", "name")
        elif self.action == "retrieve":
            return Page.objects.get_available().defer("is_available")

    # TODO: Add managers

    def get_serializer_class(self):
        if self.action == "list":
            return PageMinimalSerializer
        elif self.action == "retrieve":
            return PageReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()


class KeywordViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Keywords instances.

    Endpoints:
    - GET /api/v1/keywords/
    - POST /api/v1/keywords/
    - GET /api/v1/keywords/{id}/
    - PUT /api/v1/keywords/{id}/
    - PATCH /api/v1/keywords/{id}/
    - DELETE /api/v1/keywords/{id}/
    """

    permission_classes = [IsMarketing]
    serializer_class = KeywordWriteSerializer
    search_fields = ["name"]

    def get_queryset(self):
        return Keyword.objects.get_available()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return KeywordReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()
