"""Views for Home App."""

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema_view

from .models import Company
from .serializers import CompanyReadSerializer
from .schemas import company_schemas


@extend_schema_view(**company_schemas)
class CompanyView(APIView):
    """
    View to display all the public information of the company.

    Endpoints:
    - GET api/v1/company/
    """

    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        try:
            company = Company.objects.first()
            if company:
                serializer = CompanyReadSerializer(company)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(
                {"detail": "No company found."},
                status=status.HTTP_404_NOT_FOUND,
            )
        except Exception as e:
            return Response(
                {"error": f"{e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
