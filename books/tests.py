# books/test.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book, Review

User = get_user_model()


class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="A test description.",
            price=19.99,
        )
        self.user = User.objects.create_user(username="testuser", password="testpass123")

    def test_book_str(self):
        self.assertEqual(str(self.book), "Test Book")

    def test_average_rating_with_no_reviews(self):
        self.assertIsNone(self.book.average_rating())

    def test_average_rating_with_site_rating_fallback(self):
        self.book.site_rating = 4.5
        self.book.save()
        self.assertEqual(self.book.average_rating(), 4.5)

    def test_average_rating_with_reviews(self):
        Review.objects.create(book=self.book, user=self.user, rating=4)
        another_user = User.objects.create_user(username="user2", password="testpass123")
        Review.objects.create(book=self.book, user=another_user, rating=5)
        self.assertEqual(self.book.average_rating(), 4.5)

    def test_review_count(self):
        Review.objects.create(book=self.book, user=self.user, rating=3)
        self.assertEqual(self.book.review_count(), 1)


class BookViewsTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            price=19.99,
        )
        self.user = User.objects.create_user(username="testuser", password="testpass123")

    def test_book_list_view_status_code(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_list_view_shows_book(self):
        response = self.client.get(reverse('book_list'))
        self.assertContains(response, "Test Book")

    def test_book_detail_view_status_code(self):
        response = self.client.get(reverse('book_detail', args=[self.book.pk]))
        self.assertEqual(response.status_code, 200)

    def test_book_detail_view_shows_correct_book(self):
        response = self.client.get(reverse('book_detail', args=[self.book.pk]))
        self.assertContains(response, "Test Book")
        self.assertContains(response, "Test Author")

    def test_review_submission_requires_login(self):
        response = self.client.post(
            reverse('book_detail', args=[self.book.pk]),
            {'rating': 5, 'comment': 'Great book!'}
        )
        
        self.assertNotEqual(response.status_code, 200)

    def test_authenticated_user_can_submit_review(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse('book_detail', args=[self.book.pk]),
            {'rating': 5, 'comment': 'Great book!'}
        )
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.first().rating, 5)

    def test_user_cannot_review_same_book_twice(self):
        self.client.login(username="testuser", password="testpass123")
        Review.objects.create(book=self.book, user=self.user, rating=4)
        self.client.post(
            reverse('book_detail', args=[self.book.pk]),
            {'rating': 5, 'comment': 'Second review attempt'}
        )
        self.assertEqual(Review.objects.count(), 1) 