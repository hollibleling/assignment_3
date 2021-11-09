from rest_framework import serializers
from .models import Company, CompanyName, Tag

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