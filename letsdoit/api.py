__author__ = 'bazinga'
from rest_framework import generics, permissions
from serializers import CategorySerializer
from .models import Category
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse

"""
class CategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    permission_classes = [
        permissions.AllowAny
    ]
"""
class CategoryDetail(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def results(request):
        return render_to_response('services.html')
