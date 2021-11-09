import json

from django.http  import JsonResponse

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from company.models import *
from company.serializers import CompanyNameSerializer

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
