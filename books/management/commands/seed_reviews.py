import random
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from books.models import Book, Review

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds sample reviews for books'

    def handle(self, *args, **kwargs):
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('No users found. Create a user first (e.g. python manage.py createsuperuser).'))
            return

        comments = [
            "Really enjoyed this book!",
            "A must-read classic.",
            "Couldn't put it down.",
            "Great story, well written.",
            "Not my favorite, but still good.",
            "Highly recommend to everyone.",
            "An interesting perspective.",
            "",
        ]

        count = 0
        for book in Book.objects.all():
            if not Review.objects.filter(book=book, user=user).exists():
                Review.objects.create(
                    book=book,
                    user=user,
                    rating=random.randint(3, 5),
                    comment=random.choice(comments),
                )
                count += 1

        self.stdout.write(self.style.SUCCESS(f'{count} reviews created.'))