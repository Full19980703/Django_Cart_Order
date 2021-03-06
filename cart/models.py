from products.models import Product
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    item = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return f'{self.quantity} of {self.item.name}'

# Order Model
class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
