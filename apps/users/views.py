"""Views for Users App."""

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsClient, IsAdministrator
from apps.users.models import User
from apps.users.serializers import UserHistorySerializer
from apps.reviews.models import Review
from apps.reviews.serializers import ReviewReadSerializer
from apps.orders.models import Order
from apps.orders.serializers import OrderReadSerializer


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
