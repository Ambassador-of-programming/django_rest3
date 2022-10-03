from email.policy import default
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(max_length=127)
    price = models.PositiveIntegerField(default=0)
    articul = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    user_name = models.CharField(max_length=127)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveIntegerField(default=0)
    delivery_address = models.CharField(max_length=127)

    def __str__(self) -> str:
        return self.user_name

class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    total_price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)

    @property
    def sum_product_price(self):
        return self.product.price * self.amount

    def __str__(self) -> str:
        return self.product.name
