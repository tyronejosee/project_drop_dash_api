# """Views for Drivers App."""

# from django.db import transaction
# from django.core.cache import cache
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from drf_spectacular.utils import extend_schema_view

# from apps.utilities.functions import encrypt_field
# from apps.users.permissions import IsClient, IsDriver
# from apps.users.choices import RoleChoices
# from .models import Driver, Resource
# from .serializers import (
#     DriverReadSerializer,
#     DriverWriteSerializer,
#     ResourceReadSerializer,
#     ResourceWriteSerializer,
# )
# from .schemas import driver_create_schema


# class DriverResourceHistoryView(APIView):
#     """
#     View for retrieving a driver's resource history.

#     Endpoints:
#     - GET api/v1/drivers/resources/history/
#     """

#     permission_classes = [IsDriver]

#     def get(self, request, *args, **kwargs):
#         # Retrieve a driver's resource history
#         driver = get_object_or_404(Driver, user_id=request.user)
#         resources = Resource.objects.filter(driver_id=driver)
#         if not resources:
#             return Response(
#                 {"detail": "There are no resources available."},
#                 status=status.HTTP_404_NOT_FOUND,
#             )
#         serializer = ResourceReadSerializer(resources, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
