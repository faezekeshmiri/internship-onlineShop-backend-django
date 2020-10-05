from django.shortcuts import render
from rest_framework import viewsets
from .models import ShoppingCart, Address, User
from .serializers import ShoppingCartSerializer, AddressSerializer, UserSerializer


class ShoppingCartView(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class AddressView(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


