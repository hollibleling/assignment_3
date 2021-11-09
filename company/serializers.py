from django.db.models import fields
from company.models import Language, Tag
from rest_framework import serializers

class CompanyTagSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        return {
            'id'        : instance.id,
            'companyid' : instance.company_id,
            'tagid'     : instance.tag_id,
        }

class CompanyNameSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)

    def to_representation(self, instance):
        return {
            'id'        : instance.id,
            'companyid' : instance.company_id,
            'languageid': instance.language_id,
        }

class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10)

    class Meta:
        model = Tag
        fields = ['id', 'name']

class CompanySerializer(serializers.ModelSerializer):
    id = serializers.BigIntegerField(primary_key=True)
    tag = TagSerializer(read_only=True, many=True)
    companytag = CompanyTagSerializer(read_only=True, many=True)


class LanguageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=50)
    tag = TagSerializer(read_only=True, many=True)
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