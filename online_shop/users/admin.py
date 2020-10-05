from django.contrib import admin
from users.models import ShoppingCart, Address, User
# Register your models here.

admin.site.register(ShoppingCart)
admin.site.register(Address)
admin.site.register(User)
