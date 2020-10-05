from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from products.models import Product


class User(models.Model):
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    is_staff = models.BooleanField(default=False)
    is_producer = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.first_name + " " + self.last_name


class Address(models.Model):
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    alley = models.CharField(max_length=30)
    plaque = models.CharField(max_length=15)
    location_lat = models.FloatField(_('Latitude'), blank=True, null=True)
    location_lon = models.FloatField(_('Longitude'), blank=True, null=True)


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete= models.CASCADE)
    products = models.ManyToManyField(Product)
    discount = models.IntegerField()

    def __str__(self):
        return self.user.__str__() + " " + str(self.id)
