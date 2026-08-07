# orders/test.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from books.models import Book
from .models import Order, OrderItem

User = get_user_model()


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.book = Book.objects.create(title="Test Book", author="Author", price=15.00)
        self.order = Order.objects.create(user=self.user, total_price=30.00)

    def test_order_str(self):
        self.assertEqual(str(self.order), f"Order #{self.order.id} - testuser")

    def test_order_item_subtotal(self):
        item = OrderItem.objects.create(
            order=self.order, book=self.book, quantity=2, price_at_purchase=15.00
        )
        self.assertEqual(item.subtotal(), 30.00)


class OrderListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.other_user = User.objects.create_user(username="otheruser", password="testpass123")
        self.book = Book.objects.create(title="Test Book", author="Author", price=15.00)

        self.order = Order.objects.create(user=self.user, total_price=15.00)
        self.other_order = Order.objects.create(user=self.other_user, total_price=25.00)

    def test_order_list_requires_login(self):
        response = self.client.get(reverse('order_list'))
        self.assertNotEqual(response.status_code, 200)

    def test_order_list_shows_only_own_orders(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse('order_list'))
        self.assertContains(response, f"Order #{self.order.id}")
        self.assertNotContains(response, f"Order #{self.other_order.id}")