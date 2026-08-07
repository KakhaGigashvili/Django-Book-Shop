# cart/test.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from books.models import Book
from .models import Cart, CartItem

User = get_user_model()


class CartModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.book = Book.objects.create(title="Test Book", author="Author", price=10.00)
        self.cart = Cart.objects.create(user=self.user)

    def test_cart_str(self):
        self.assertEqual(str(self.cart), "Cart of testuser")

    def test_cart_item_subtotal(self):
        item = CartItem.objects.create(cart=self.cart, book=self.book, quantity=3)
        self.assertEqual(item.subtotal(), 30.00)

    def test_cart_total_price(self):
        book2 = Book.objects.create(title="Book 2", author="Author 2", price=5.00)
        CartItem.objects.create(cart=self.cart, book=self.book, quantity=2)  
        CartItem.objects.create(cart=self.cart, book=book2, quantity=1)    
        self.assertEqual(self.cart.total_price(), 25.00)


class CartViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.book = Book.objects.create(title="Test Book", author="Author", price=10.00)
        self.client.login(username="testuser", password="testpass123")

    def test_add_to_cart_creates_cart_item(self):
        self.client.post(reverse('add_to_cart', args=[self.book.pk]))
        self.assertEqual(CartItem.objects.count(), 1)

    def test_add_to_cart_twice_increases_quantity(self):
        self.client.post(reverse('add_to_cart', args=[self.book.pk]))
        self.client.post(reverse('add_to_cart', args=[self.book.pk]))
        item = CartItem.objects.first()
        self.assertEqual(item.quantity, 2)

    def test_cart_detail_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('cart_detail'))
        self.assertNotEqual(response.status_code, 200)

    def test_cart_detail_shows_items(self):
        self.client.post(reverse('add_to_cart', args=[self.book.pk]))
        response = self.client.get(reverse('cart_detail'))
        self.assertContains(response, "Test Book")

    def test_remove_from_cart(self):
        self.client.post(reverse('add_to_cart', args=[self.book.pk]))
        item = CartItem.objects.first()
        self.client.post(reverse('remove_from_cart', args=[item.id]))
        self.assertEqual(CartItem.objects.count(), 0)

    def test_remove_from_cart_only_own_items(self):
        other_user = User.objects.create_user(username="otheruser", password="testpass123")
        other_cart = Cart.objects.create(user=other_user)
        other_item = CartItem.objects.create(cart=other_cart, book=self.book, quantity=1)

        response = self.client.post(reverse('remove_from_cart', args=[other_item.id]))
        self.assertEqual(response.status_code, 404) 
        self.assertEqual(CartItem.objects.count(), 1)  


class CheckoutTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123", balance=100)
        self.book = Book.objects.create(title="Test Book", author="Author", price=30.00)
        self.client.login(username="testuser", password="testpass123")

    def test_checkout_with_sufficient_balance(self):
        self.client.post(reverse('add_to_cart', args=[self.book.pk]))
        response = self.client.post(reverse('checkout'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.balance, 70.00) 
        self.assertEqual(CartItem.objects.count(), 0)  

    def test_checkout_with_insufficient_balance(self):
        expensive_book = Book.objects.create(title="Expensive Book", author="Author", price=500.00)
        self.client.post(reverse('add_to_cart', args=[expensive_book.pk]))
        self.client.post(reverse('checkout'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.balance, 100) 
        self.assertEqual(CartItem.objects.count(), 1) 

    def test_checkout_empty_cart(self):
        response = self.client.post(reverse('checkout'))
        self.assertRedirects(response, reverse('cart_detail'))