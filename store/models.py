from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def subtotal(self):
        return self.product.price * self.quantity

    @property
    def subtotal_value(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name} ({self.user.username})"
