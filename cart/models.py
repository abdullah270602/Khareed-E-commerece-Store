from django.db import models
from django.contrib.auth.models import User
import uuid
from products.models import Product
from django.db.models import F, Sum

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, editable= False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_cart')
    is_paid = models.BooleanField(default=False)
    
    def get_total_items(self):
        return CartItem.objects.filter(cart=self).aggregate(total_items=models.Sum('quantity'))['total_items'] or 0
    
    
    def get_total_cost(self):
        total_cost = CartItem.objects.filter(cart=self).aggregate(total=Sum(F(('product__price')) * F(('quantity'))))['total']
        return total_cost or 0
    
    
    def __str__(self) -> str:
        return str(self.user)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name='cart_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    
    def __str__(self) -> str:
        return (f"QTY: {self.quantity} -> {self.product}")

