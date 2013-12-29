
__author__ = 'bazinga'
from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField
    photo= serializers.ImageField

    class Meta:
        model = Category
        fields = ('id', 'servicename', 'categoryImage')
        read_only_fields = ('id', 'servicename')