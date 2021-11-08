from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from company.models import *


class SearchView(View):
    def get(self, request):
        word = request.Get.get('queary', '')
        lists = []

        name_ko = Company.objects.filter(korean_name__icontains = word)
        name_en = Company.objects.filter(english_name__icontains = word)
        name_ja = Company.objects.filter(japanies_name__icontains = word)

        if not name_ko.exists() and name_en.exists() and name_ja.exists():
            return JsonResponse({"Message" : ""}, status=200)

        if name_ko.exists():
            products = name_ko
            for product in products:
                results.append(product.korean_name)

        if name_en.exists():
            products  = name_en
            for product in products:
                results.append(product.korean_name)
        
        if name_ja.exists():
            products  = name_ja
            for product in products:
                results.append(product.korean_name)

        return JsonResponse({"results" : lists}, status=200)
