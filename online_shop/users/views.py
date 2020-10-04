from django.shortcuts import render
from rest_framework import viewsets
from .models import ShoppingCart, Address
from .serializers import ShoppingCartSerializer, AddressSerializer, CustomUserSerializer
from django.conf import settings


class ShoppingCartView(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class CustomUserView(viewsets.ModelViewSet):
    queryset = settings.AUTH_USER_MODEL.objects.all().order_by('date_joined')
    serializer_class = CustomUserSerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer