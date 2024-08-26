"""ViewSets for Promotions App."""

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsAdministrator
from apps.utilities.mixins import CacheMixin, LogicalDeleteMixin
from apps.utilities.helpers import generate_cache_key
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
from .schemas import country_schemas, state_schemas, city_schemas


@extend_schema_view(**country_schemas)
class CountryViewSet(CacheMixin, LogicalDeleteMixin, ModelViewSet):
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
        return Country.objects.get_available()

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

    def get_cache_key(self, request, *args, **kwargs):
        return generate_cache_key(request, prefix="country")


@extend_schema_view(**state_schemas)
class StateViewSet(CacheMixin, LogicalDeleteMixin, ModelViewSet):
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

    def get_queryset(self):
        if self.action == "list":
            return State.objects.get_list()
        return State.objects.get_detail()

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

    def get_cache_key(self, request, *args, **kwargs):
        return generate_cache_key(request, prefix="state")


@extend_schema_view(**city_schemas)
class CityViewSet(CacheMixin, LogicalDeleteMixin, ModelViewSet):
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

    def get_queryset(self):
        if self.action == "list":
            return City.objects.get_list()
        return City.objects.get_detail()

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

    def get_cache_key(self, request, *args, **kwargs):
        return generate_cache_key(request, prefix="city")
