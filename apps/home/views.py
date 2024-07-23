"""Views for Home App."""

from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import Keyword
from .serializers import KeywordMinimalSerializer


class KeywordView(ListAPIView):
    """
    View to manage the driver profile.

    Endpoints:
    - GET api/v1/keywords/
    """

    permission_classes = [AllowAny]
    serializer_class = KeywordMinimalSerializer

    def get_queryset(self):
        return Keyword.objects.get_available()[:10]
