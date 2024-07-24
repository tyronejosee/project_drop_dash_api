"""ViewSets for Promotions App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from apps.users.permissions import IsAdministrator
from apps.utilities.mixins import ListCacheMixin, LogicalDeleteMixin
from .models import Country, State, City
from .serializers import (
    CountryReadSerializer,
    CountryWriteSerializer,
    CountryMinimalSerializer,
    StateReadSerializer,
    StateWriteSerializer,
    StateMinimalSerializer,
    CityReadSerializer,
    CityWriteSerializer,
    CityMinimalSerializer,
)


class CountryViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing Country instances.

    Endpoints:
    - GET /api/v1/countries/
    - POST /api/v1/countries/
    - GET /api/v1/countries/{id}/
    - PUT /api/v1/countries/{id}/
    - PATCH /api/v1/countries/{id}/
    - DELETE /api/v1/countries/{id}/
    """

    permission_classes = [IsAdministrator]
    serializer_class = CountryWriteSerializer
    search_fields = ["name"]

    def get_queryset(self):
        return Country.objects.get_available().defer("is_available")

    def get_serializer_class(self):
        if self.action == "list":
            return CountryMinimalSerializer
        elif self.action == "retrieve":
            return CountryReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()


class StateViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing State instances.

    Endpoints:
    - GET /api/v1/states/
    - POST /api/v1/states/
    - GET /api/v1/states/{id}/
    - PUT /api/v1/states/{id}/
    - PATCH /api/v1/states/{id}/
    - DELETE /api/v1/states/{id}/
    """

    permission_classes = [IsAdministrator]
    serializer_class = StateWriteSerializer
    search_fields = ["name"]
    # filterset_class = StateFilter # TODO: Add filter

    def get_queryset(self):
        return State.objects.get_available().select_related(
            "country_id"
        )  # TODO: Add manager

    def get_serializer_class(self):
        if self.action == "list":
            return StateMinimalSerializer
        elif self.action == "retrieve":
            return StateReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()


class CityViewSet(ListCacheMixin, LogicalDeleteMixin, ModelViewSet):
    """
    ViewSet for managing City instances.

    Endpoints:
    - GET /api/v1/cities/
    - POST /api/v1/cities/
    - GET /api/v1/cities/{id}/
    - PUT /api/v1/cities/{id}/
    - PATCH /api/v1/cities/{id}/
    - DELETE /api/v1/cities/{id}/
    """

    permission_classes = [IsAdministrator]
    serializer_class = CityWriteSerializer
    search_fields = ["name"]
    # filterset_class = CityFilter # TODO: Add filter

    def get_queryset(self):
        return City.objects.select_related(
            "state_id"
        ).get_available()  # TODO: Add manager

    def get_serializer_class(self):
        if self.action == "list":
            return CityMinimalSerializer
        elif self.action == "retrieve":
            return CityReadSerializer
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return super().get_permissions()
