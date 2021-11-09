from django.db.models.deletion import RESTRICT
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CompanyName
from .serializers import CompanySearchSerializers

class CompanySearchView(APIView):
    def get(self, request, name):
        language = request.headers.get("x-wanted-language", "ko")
        if not CompanyName.objects.filter(name=name, language__name=language).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        company = CompanyName.objects.filter(name=name, language__name=language)

        serializer = CompanySearchSerializers(company, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

