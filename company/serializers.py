from company.models import *
from rest_framework import serializers


class CompanyTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTag
        fields = ['id', 'company', 'tag']


class CompanyNameSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField()

    class Meta:
        model  = CompanyName
        fields = ['company_name']

    def get_company_name(self, obj):
        return obj.name


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
    # tags = TagSerializer(read_only=True, many=True)
    # company_name = CompanyTagSerializer(read_only=True, many=True)

    class Meta:
        model = Company
        fields = ['id']

    def to_internal_value(self, data):
        return data

    def create(self, validated_data):
        company = Company.objects.create()
        for i in validated_data['company_name'].keys():
            language = Language.objects.get_or_create(name=i)[0]
            CompanyName.objects.create(name=validated_data['company_name'][i], company=company, language=language)

        for i in validated_data['tags']:
            for j in i['tag_name'].keys():
                language = Language.objects.get_or_create(name=j)[0]
                tag = Tag.objects.create(name=i['tag_name'][j], language=language)
                CompanyTag.objects.create(company=company, tag=tag)

        return company

    def to_representation(self, instance):
        return {
            "company_name": instance.companyname_set.get(language__name=self.validated_data['lang']).name,
            "tags": [i.tag.name for i in instance.companytag_set.filter(tag__language__name='tw')]
        }


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
