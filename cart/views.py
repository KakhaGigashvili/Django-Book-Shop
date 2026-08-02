# cart/view.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from books.models import Book 
from .models import Cart, CartItem
from django.contrib import messages
from orders.models import Order, OrderItem

@login_required
def add_to_cart(requset, book_id):
    book = get_object_or_404(Book, pk=book_id)
    cart, created = Cart.objects.get_or_create(user=requset.user)
    item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)
    
    if not item_created:
        item.quantity += 1
        item.save()
        
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, cart__user = request.user)
    item.delete()
    return redirect('cart_detail')

@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()

    if not items.exists():
        messages.error(request, "Your cart is empty.")
        return redirect('cart_detail')

    total = cart.total_price()

    if request.user.balance < total:
        messages.error(request, "Insufficient balance. Please add more funds.")
        return redirect('cart_detail')

    order = Order.objects.create(user=request.user, total_price=total)

    for item in items:
        OrderItem.objects.create(
            order=order,
            book=item.book,
            quantity=item.quantity,
            price_at_purchase=item.book.price,
        )

    request.user.balance -= total
    request.user.save()

    items.delete()

    messages.success(request, f"Order #{order.id} placed successfully!")
    return redirect('order_list')