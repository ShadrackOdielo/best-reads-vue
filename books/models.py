from django.conf import settings
from django.db import models


class Book(models.Model):
    isbn = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    authors = models.TextField()  # Storing multiple authors as a comma-separated string
    description = models.TextField(default="no description")
    published_date = models.DateField(null=True, blank=True)
    categories = models.TextField()  # Storing multiple categories as a comma-separated string
    average_rating = models.FloatField(null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)
    preview_url = models.URLField(null=True, blank=True)


class UserBook(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    status_choices = [
        ("READ", "Read"),
        ("TO_READ", "To Read"),
        ("READING", "Currently Reading"),
        ("NOT_FINISH", "Did Not Finish"),
        ("LIKED", "Liked"),
    ]
    status = models.CharField(max_length=10, choices=status_choices)
    rating = models.IntegerField(null=True, blank=True)
    review = models.TextField(null=True, blank=True)


# Add other models as needed, such as Review, Category, etc.
