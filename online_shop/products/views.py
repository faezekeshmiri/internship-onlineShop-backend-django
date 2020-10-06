from django.shortcuts import render
from rest_framework import viewsets
from .models import MyProduct, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = MyProduct.objects.all().order_by('date')
    serializer_class = ProductSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
