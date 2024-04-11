"""Views for Menus App."""

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Menu
from .serializers import MenuSerializer


class MenuAPIView(APIView):
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Menu.objects.filter(available=True)

    def get(self, request, format=None):
        """Get a list of playlists."""
        menu = self.get_queryset()
        serializer = self.serializer_class(menu, many=True)
        return Response(serializer.data)
