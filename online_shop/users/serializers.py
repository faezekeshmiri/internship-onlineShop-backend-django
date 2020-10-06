from rest_framework import serializers
from .models import ShoppingCart, Address


class ShoppingCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ['id', 'url', 'user', 'address', 'products', 'discount']


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'url', 'city', 'street', 'alley', 'plaque', 'location_lat', 'location_lon']
