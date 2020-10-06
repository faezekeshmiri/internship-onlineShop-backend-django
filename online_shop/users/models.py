from django.db import models
from django.utils.translation import gettext_lazy as _
from products.models import MyProduct
from django.conf import settings


class Address(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    alley = models.CharField(max_length=30)
    plaque = models.CharField(max_length=15)
    location_lat = models.FloatField(_('Latitude'), blank=True, null=True)
    location_lon = models.FloatField(_('Longitude'), blank=True, null=True)


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    products = models.ManyToManyField(MyProduct)
    discount = models.IntegerField()

    def __str__(self):
        return self.user.__str__() + " " + str(self.id)
