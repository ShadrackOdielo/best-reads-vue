# books/views.py
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Book  # Import your Book model
from .services.google_books import get_book, get_latest_books, get_popular_books, search_books


class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

    def get_queryset(self):
        popular_books = get_popular_books()
        latest_books = get_latest_books()
        return popular_books + latest_books  # Combine popular and latest books


def search(request):
    query = request.GET.get("q", "")
    books = search_books(query)
    return render(request, "books/book_search_results.html", {"query": query, "books": books})


class BookDetailView(DetailView):
    model = Book
    pk = "google_id"
    book = get_book(pk)
    template_name = "books/book_detail.html"
