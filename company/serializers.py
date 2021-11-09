from rest_framework import serializers
from company.models import *

class CompanySearchSerializers(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = CompanyName
        fields = ['company_name', 'tags']

    def get_tags(self, obj):
        company = Company.objects.get(id=obj.company_id)
        tag = Tag.objects.filter(companytag__company=company)
        return [i.name for i in tag]
        
    def get_company_name(self, obj):
        return obj.name


class CompanyNameSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = CompanyName
        fields = ['id', 'name', 'company', 'language']
    
