from django.shortcuts import render
from rest_framework import viewsets
from .models import ShoppingCart, Address
from .serializers import ShoppingCartSerializer, AddressSerializer


class ShoppingCartView(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


