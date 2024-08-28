"""Views for Payments App."""

from django.conf import settings
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import mercadopago

from apps.users.permissions import IsClient
from apps.orders.models import Order
from apps.orders.serializers import OrderReadSerializer
from apps.deliveries.models import Delivery
from apps.deliveries.choices import StatusChoices


# https://github.com/mercadopago/sdk-python
sdk = mercadopago.SDK(settings.MERCADOPAGO_ACCESS_TOKEN)


class PaymentView(APIView):
    """
    View to handle the payment of an order.

    Endpoints:
    """

    permission_classes = [IsClient]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        # TODO: Add services layers
        user = request.user
        data = request.data

        # Body
        order_id = data.get("order_id")
        token = data.get("token")
        payment_method_id = data.get("payment_method_id")
        installments = data.get("installments", 1)
        issuer_id = data.get("issuer_id", None)

        try:
            # Retrieve the order
            order = get_object_or_404(Order, id=order_id, user_id=user)

            # Check if the order has already been paid
            if order.is_payment:
                return Response(
                    {"error": "Order is already paid."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Create the payment using MercadoPago
            payment_data = {
                "transaction_amount": float(order.amount),
                "token": token,
                "installments": int(installments),
                "payment_method_id": payment_method_id,
                "issuer_id": issuer_id,
                "payer": {
                    "email": user.email,
                    "identification": {
                        "type": "DNI",
                        "number": user.profile.identification_number,
                    },
                },
            }

            payment_response = sdk.payment().create(payment_data)
            payment = payment_response["response"]

            if payment["status"] == "approved":
                # Mark the order as paid
                order.is_payment = True
                order.status = "COMPLETED"
                order.transaction = payment["id"]
                order.save()

                # Create a record in the Delivery model
                Delivery.objects.create(
                    order_id=order,
                    status=StatusChoices.PENDING,
                )

                order_serializer = OrderReadSerializer(order)
                return Response(order_serializer.data, status=status.HTTP_200_OK)

            return Response(
                {"error": "Payment failed"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as e:
            return Response(
                {"error": f"{e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
