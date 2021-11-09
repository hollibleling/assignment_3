from rest_framework import serializers

from company.models import *

class CompanyNameSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = CompanyName
        fields = ['id', 'name', 'company', 'language']
    