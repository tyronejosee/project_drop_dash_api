"""Views for Restaurants App."""

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status

from apps.utilities.pagination import LargeSetPagination
from apps.categories.models import Category
# from apps.categories.serializers import CategorySerializer
# from apps.menus.models import Menu
# from apps.menus.serializers import MenuSerializer
from .models import Restaurant
from .serializers import RestaurantSerializer
from .permissions import IsBusinessOwnerOrReadOnly


class RestaurantListAPIView(APIView):
    """APIView to list and create restaurants."""
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        # Get a list of restaurants
        stores = Restaurant.objects.filter(available=True).order_by("id")
        paginator = LargeSetPagination()
        page = paginator.paginate_queryset(stores, request)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": "No restaurants available."},
            status=status.HTTP_204_NO_CONTENT
        )

    def post(self, request):
        # Create a new restaurant
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class RestaurantDetailAPIView(APIView):
    """APIView to retrieve, update, and delete a restaurant."""
    serializer_class = RestaurantSerializer
    permission_classes = [IsBusinessOwnerOrReadOnly]

    def get_object(self, restaurant_id):
        # Get a restaurant instance by id
        try:
            return Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, restaurant_id):
        """Get details of a restaurant."""
        store = self.get_object(restaurant_id)
        serializer = self.serializer_class(store)
        return Response(serializer.data)

    def put(self, request, restaurant_id):
        """Update a restaurant."""
        store = self.get_object(restaurant_id)
        serializer = self.serializer_class(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, restaurant_id):
        """Delete a restaurant."""
        store = self.get_object(restaurant_id)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RestaurantCategoriesAPIView(APIView):

    def get(self, request, restaurant_id, formate=None):
        # Gets a list of categories associated with a restaurant
        categories = Category.filter(restaurant=restaurant_id)
        paginator = LargeSetPagination()
        paginated_data = paginator.paginate_queryset(categories, request)
        if paginated_data is not None:
            serializer = self.serializer_class(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)
        return Response(
            {"detail": "No categories available."},
            status=status.HTTP_204_NO_CONTENT
        )


# class RestaurantMenuAPIView(APIView):
#     # permission_classes = []

#     def get(self, request, restaurant_id, format=None):
#         try:
#             menu = Menu.objects.get(restaurant=restaurant_id)
#             menu_items = MenuItem.objects.filter(menu=menu)
#             serializer = MenuItemSerializer(menu_items, many=True)
#             return Response(serializer.data)
#         except Menu.DoesNotExist:
#             return Response(
#                 status=status.HTTP_404_NOT_FOUND
#             )
