from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from company.models import *


class SearchView(View):
    def get(self, request):
        word = request.GET.get('queary')
        lists = []

        if word == "":
            return JsonResponse({"Message" : ""}, status=200)

        name = CompanyName.objects.filter(name__icontains = word)

        if not name.exists():
            return JsonResponse({"Message" : ""}, status=200)

        if name.exists():
            products = name
            for product in products:
                lists.append(product.name)

        return JsonResponse({"results" : lists}, status=200)
