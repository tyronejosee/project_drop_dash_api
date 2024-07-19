"""Views for Orders App."""

from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.users.permissions import IsClient
from apps.restaurants.models import Food, Restaurant
from apps.locations.models import Country, State, City
from .models import Order, OrderItem
from .serializers import OrderReadSerializer


class OrderCreateView(APIView):
    """Pending."""

    permission_classes = [IsClient]

    def get(self, request):
        """Get my orders."""
        orders = (
            Order.objects.select_related(
                "user_id", "restaurant_id", "city_id", "state_id", "country_id"
            )
            .prefetch_related("orderitem_set__food")
            .filter(user_id=request.user)
        )
        serializer = OrderReadSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        data = request.data

        with transaction.atomic():
            restaurant = get_object_or_404(Restaurant, id=data["restaurant"])
            city = get_object_or_404(City, id=data["city"])
            state = get_object_or_404(State, id=data["state"])
            country = get_object_or_404(Country, id=data["country"])

            order = Order.objects.create(
                user_id=user,
                restaurant_id=restaurant,
                address=data["address"],
                city_id=city,
                state_id=state,
                country_id=country,
                phone=data["phone"],
                note=data.get("note", ""),
                payment_method=data["payment_method"],
            )

            if not order:
                return Response(
                    {"detail": "Failed to create order"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            foods_data = data.get("foods", [])
            order_items = []
            subtotal = 0

            for item in foods_data:
                food = get_object_or_404(Food, id=item["food"])
                quantity = item["quantity"]
                price = food.price

                order_item = OrderItem(
                    order_id=order,
                    food_id=food,
                    quantity=quantity,
                    price=price,
                    subtotal=price * quantity,
                )
                order_items.append(order_item)
                subtotal += order_item.subtotal

            OrderItem.objects.bulk_create(order_items)

            # Update order subtotal
            order.subtotal = subtotal
            order.save()

        return Response(
            {"detail": "Order created successfully"},
            status=status.HTTP_201_CREATED,
        )
