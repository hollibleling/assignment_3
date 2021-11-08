from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Language, Company, CompanyName, CompanyTag, Tag

class LanguageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyNameSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyName
        fields = '__all__'

class CompanyTagSerializers(serializers.ModelSerializer):
    class Meta:
        model = CompanyTag
        fields = '__all__'

class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'