from rest_framework import serializers
from .models import CustomUser, ShoppingCart, Address


class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'url', 'first_name', 'last_name', 'phone', 'email', 'is_staff', 'is_producer', 'is_active', 'date_joined']


class ShoppingCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'url', 'user', 'address', 'products', 'discount']


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'url', 'city', 'street', 'alley', 'plaque', 'location_lat', 'location_lon']
