"""Views for Orders App."""

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsClient
from apps.restaurants.models import Food, Restaurant
from apps.locations.models import Region, Comune
from .models import Order, OrderItem


class OrderCreateView(APIView):
    """Pending."""
    permission_classes = [IsClient]

    # TODO: Refactor
    def post(self, request):
        # Create a order
        user = request.user
        data = request.data

        restaurant_id = data["restaurant"]
        comune_id = data["comune"]
        region_id = data["region"]

        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        comune = get_object_or_404(Comune, id=comune_id)
        region = get_object_or_404(Region, id=region_id)

        order = Order(
            user=user,
            restaurant=restaurant,
            address=data["address"],
            comune=comune,
            region=region,
            phone=data["phone"],
            note=data.get("note", ""),
            payment_method=data["payment_method"]
        )
        order.save()

        foods_data = data.get("foods", [])
        if foods_data:
            for item in foods_data:
                food_id = item["food"]
                quantity = item["quantity"]

                food = get_object_or_404(Food, id=food_id)

                order_item = OrderItem(
                    order=order,
                    food=food,
                    quantity=quantity
                )
                order_item.save()

        return Response({"detail": "Order created successfully"}, status=status.HTTP_201_CREATED)
