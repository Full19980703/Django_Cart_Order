from cart.models import Cart, Order
from products.models import Category, Product
from django.contrib import admin

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
