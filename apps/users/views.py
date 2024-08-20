"""Views for Users App."""

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djoser.social.views import ProviderAuthView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.utils import extend_schema_view

from apps.users.permissions import IsClient, IsAdministrator
from apps.users.models import User
from apps.users.serializers import UserHistorySerializer
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer
from apps.orders.models import Order, OrderReport
from apps.orders.serializers import OrderReadSerializer, OrderReportReadSerializer
from .schemas import (
    token_obtain_pair_schemas,
    token_refresh_schemas,
    token_verify_schemas,
    provider_auth_schemas,
)


@extend_schema_view(**token_obtain_pair_schemas)
class TokenObtainPairExtensionView(TokenObtainPairView):
    """
    Extended view for obtaining JWT tokens.

    Extends the standard TokenObtainPairView in `rest_framework_simplejwt.views`
    to include custom schema documentation using drf-spectacular.
    """

    pass


@extend_schema_view(**token_refresh_schemas)
class TokenRefreshExtensionView(TokenRefreshView):
    """
    Extended view for refreshing JWT tokens.

    Extends the standard TokenRefreshView in `rest_framework_simplejwt.views`
    to include custom schema documentation using drf-spectacular.
    """

    pass


@extend_schema_view(**token_verify_schemas)
class TokenVerifyExtensionView(TokenVerifyView):
    """
    Extended view for verifying JWT tokens.

    Extends the standard TokenVerifyView in `rest_framework_simplejwt.views`
    to include custom schema documentation using drf-spectacular.
    """

    pass


@extend_schema_view(**provider_auth_schemas)
class ProviderAuthExtensionView(ProviderAuthView):
    """
    Extended view for handling social authentication provider requests.

    Extends the standard ProviderAuthView `djoser.social.urls`
    to include custom schema documentation using drf-spectacular.
    """

    pass


class UserReviewsView(ListAPIView):
    """
    View to list all reviews of a user.

    Endpoints:
    - GET api/v1/accounts/reviews/
    """

    permission_class = [IsClient]
    serializer_class = ReviewReadSerializer
    # filterset_class = ReviewFilter

    def get_queryset(self):
        return Review.objects.filter(user_id=self.request.user)


class UserOrdersView(ListAPIView):
    """
    View to list all orders of a user.

    Endpoints:
    - GET api/v1/accounts/orders/
    """

    permission_class = [IsClient]
    serializer_class = OrderReadSerializer
    # filterset_class = OrderFilter

    def get_queryset(self):
        return Order.objects.filter(user_id=self.request.user)


class UserOrderReportsView(ListAPIView):
    """
    View to list all order reports of a user.

    Endpoints:
    - GET api/v1/accounts/order_reports/
    """

    permission_class = [IsClient]
    serializer_class = OrderReportReadSerializer

    def get_queryset(self):
        return OrderReport.objects.get_by_user(self.request.user)


class UserHistoryView(APIView):
    """
    View to list all history of a user.

    Endpoints:
    - GET api/v1/accounts/{id}/history/
    """

    permission_class = [IsAdministrator]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        history = user.history.all()
        serializer = UserHistorySerializer(history, many=True)
        return Response(serializer.data)
