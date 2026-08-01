# cart/models.py
from django.db import models
from django.conf import settings
from books.models import Book

class Cart(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart of {self.user.username}"
    
    def total_price(self):
        return sum(item.subtotal() for item in self.items.all())
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    
    class Meta:
        unique_together = ('cart', 'book')
        
    def __str__(self):
        return f"{self.quantity} x {self.book.title}"
    
    def subtotal(self):
        return self.book.price * self.quantity