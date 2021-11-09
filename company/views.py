from django.db.models.deletion import RESTRICT
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from company.serializers import CompanyNameSerializer, CompanySearchSerializers
from company.models import *

import json

from django.http  import JsonResponse


class CompanyViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):

    serializer_class = CompanyNameSerializer
    queryset = CompanyName.objects.all()

    def get_queryset(self):
        word = self.request.query_params.get('queary', None)
        lang = self.request.headers['x-wanted-language']
        lists = []

        if word == "":
            name = ""
            return name

        if lang == 'ko':
            name = CompanyName.objects.filter(name__icontains = word, language_id = 1)
        elif lang == 'en':
            name = CompanyName.objects.filter(name__icontains = word, language_id = 2)
        elif lang == 'ja':
            name = CompanyName.objects.filter(name__icontains = word, language_id = 3)

        if not name.exists():
            name = ""
            return name

        if name.exists():
            products = name
            for product in products:
                lists.append(product.name)

        return name

class CompanySearchView(APIView):
    def get(self, request, name):
        language = request.headers.get("x-wanted-language", "ko")
        if not CompanyName.objects.filter(name=name, language__name=language).exists():
            return Response(status=status.HTTP_404_NOT_FOUND)
        company = CompanyName.objects.filter(name=name, language__name=language)

        serializer = CompanySearchSerializers(company, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
