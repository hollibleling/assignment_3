from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from company.models import *
from company.serializers import CompanyNameSerializer, CompanySearchSerializers


class CompanyViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    serializer_class = CompanyNameSerializer
    queryset = CompanyName.objects.all()

    def get_queryset(self):
        word = self.request.query_params.get('query', None)
        lang = self.request.headers['x-wanted-language']
        if word == "":
            raise Exception('Not data')

        if lang == 'ko':
            name = CompanyName.objects.filter(name__icontains = word, language_id = 1)
        elif lang == 'en':
            name = CompanyName.objects.filter(name__icontains = word, language_id = 2)
        elif lang == 'ja':
            name = CompanyName.objects.filter(name__icontains = word, language_id = 3)

        if not name.exists():
            raise Exception('Not data')

        return name


class CompanySearchView(APIView):
    def get(self, request, name):
        language = request.headers.get("x-wanted-language", "ko")
        if not CompanyName.objects.filter(name=name).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)

        instance = CompanyName.objects.get(name=name).company
        company = CompanyName.objects.get(company=instance, language__name=language)
        serializer = CompanySearchSerializers(company)
        return Response(serializer.data, status=status.HTTP_200_OK)
