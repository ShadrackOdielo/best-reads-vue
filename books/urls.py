# books/urls.py
from django.urls import path

from .views import BookDetailView, BookListView, search

app_name = "books"
urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("search/", search, name="search"),
    path("<str:pk>/", BookDetailView.as_view(), name="book_detail"),
]
