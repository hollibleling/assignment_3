from rest_framework import status
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from company.models import *
from company.serializers import CompanyNameSerializer, CompanySearchSerializers, CompanySerializer


class CompanyViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):

    serializer_class = CompanySerializer
    queryset = CompanyName.objects.all()
    lookup_url_kwarg = 'company_name'

    def get_object(self, name):
        try:
            return CompanyName.objects.get(name=name).company
        except CompanyName.DoesNotExist:
            return None

    def create(self, request, *args, **kwargs):
        self.request.data.setdefault('lang', self.request.headers["x-wanted-language"])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object(kwargs['company_name'])
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        language = request.headers.get("x-wanted-language", "ko")
        company = CompanyName.objects.get(company=instance, language__name=language)
        serializer = CompanySearchSerializers(company)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanySearchViewSet(ListModelMixin, GenericViewSet):

    serializer_class = CompanyNameSerializer
    queryset = CompanyName.objects.all()
    lookup_url_kwarg = 'company_name'

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
