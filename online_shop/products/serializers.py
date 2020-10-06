from rest_framework import serializers
from .models import MyProduct, Category


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyProduct
        fields = ['id', 'url', 'name', 'price', 'image', 'description', 'category', 'date', 'producer']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'url', 'name', 'image']
