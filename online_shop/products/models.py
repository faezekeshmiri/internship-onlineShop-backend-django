from django.db import models
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.name


class MyProduct(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.ImageField()
    description = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    producer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


