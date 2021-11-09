from django.db.models import fields
from company.models import *
from rest_framework import serializers

class CompanyTagSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {
            'id'        : instance.id,
            'companyid' : instance.company_id,
            'tagid'     : instance.tag_id,
        }

class CompanyNameSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model  = CompanyName
        fields = ['company_name']

    def get_company_name(self, obj):
        return obj.name

    def to_representation(self, instance):
        return {
            'id'          : instance.id,
            'company_name': instance.name,
            'companyid'   : instance.company_id,
            'languageid'  : instance.language_id,
        }

class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10)

    class Meta:
        model = Tag
        fields = ['id', 'name']

    def to_representation(self, instance):
        return {
            'id'        : instance.id,
            'tag_name'  : instance.name,
            'languageid': instance.language_id,
        }

class CompanySerializer(serializers.ModelSerializer):
    id         = serializers.BigIntegerField(primary_key=True)
    tag        = TagSerializer(read_only=True, many=True)
    companytag = CompanyTagSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = ['id']

    def to_representation(self, instance):
        return {
            'id'        : instance.id,
        }

    def create(self, validated_data):
        companyname = validated_data
        company = Company.objects.create()
        korean = Language.objects.get_or_create(name=validated_data[''])
        english = Language.objects.get_or_create(name=validated_data[''])
        tw = Language.objects.get_or_create(name=validated_data[''])
        Tag.objects.create()
        
class LanguageSerializer(serializers.ModelSerializer):
    name    = serializers.CharField(max_length=50)
    tag     = TagSerializer(read_only=True, many=True)
    company = CompanySerializer(read_only=True, many=True)

    class Meta:
        model = Language
        fields = ['id', 'name']

    def to_representation(self, instance):
        return {
            'id'        : instance.id,
            'name'      : instance.name,
            'tagid'     : instance.tag_id,
        }

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
