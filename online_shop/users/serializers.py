from rest_framework import serializers
from .models import User, ShoppingCart, Address


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'first_name', 'last_name', 'phone', 'email', 'is_staff', 'is_producer', 'is_active', 'date_joined']


class ShoppingCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'url', 'user', 'address', 'products', 'discount']


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'url', 'city', 'street', 'alley', 'plaque', 'location_lat', 'location_lon']
