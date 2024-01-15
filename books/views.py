import requests
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .models import UserBook


class HomePageView(View):
    template_name = "books/home.html"

    def get(self, request, *args, **kwargs):
        # Fetch latest books (example: last 5 books)
        print("no code here")
        latest_books = self.fetch_latest_books()

        # Fetch popular books this week using NYT best sellers API
        popular_books = self.fetch_nyt_best_sellers()

        # Fetch personalized recommendations for registered users
        if request.user.is_authenticated:
            personalized_books = self.fetch_personalized_recommendations(request.user)
        else:
            personalized_books = []

        context = {
            "latest_books": latest_books,
            "popular_books": popular_books,
            "personalized_books": personalized_books,
        }

        return render(request, "books/home.html", context)

    def fetch_latest_books(self):
        # Implement logic to fetch the latest books (from your database or external API)
        # For example, fetch the last 5 books added to your database
        # You can use Google Books API for this example
        api_url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            "q": "subject:fiction",
            # 'key': settings.GOOGLE_BOOKS_API_KEY,
            # filter only books with an isbn10 or isbn13 number
            "maxResults": 10,
            "orderBy": "newest",
        }
        response = requests.get(api_url, params=params)
        data = response.json()

        return data.get("items", [])

    def fetch_nyt_best_sellers(self):
        # Implement logic to fetch popular books this week from NYT best sellers API
        # You need to sign up for a NYT Developer account to get your API key
        nyt_api_key = settings.NYT_API_KEY
        api_url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json"
        params = {"api-key": nyt_api_key, "api-secret": settings.NYT_API_SECRET}
        response = requests.get(api_url, params=params)
        data = response.json()
        print("this worked too")
        return data.get("results", {}).get("books", [])

    def fetch_personalized_recommendations(self, user):
        # Implement logic to fetch personalized recommendations for the user
        # You need to implement your recommendation logic, for now, let's fetch some random books
        api_url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            # 'key': settings.GOOGLE_BOOKS_API_KEY,
            "maxResults": 20,
            "orderBy": "relevance",
        }
        response = requests.get(api_url, params=params)
        data = response.json()

        return data.get("items", [])


class BookDetailView(View):
    template_name = "book_detail.html"

    def get(self, request, isbn, *args, **kwargs):
        book_data = self.fetch_google_books_data(isbn)

        if book_data:
            return render(request, "books/book_detail.html", {"book": book_data})
        else:
            # Handle the case where book data couldn't be fetched
            return render(request, "book_not_found.html")  # Create a book_not_found template

    def fetch_google_books_data(self, isbn):
        api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
        response = requests.get(api_url)
        data = response.json()

        if "items" in data:
            return data["items"][0]["volumeInfo"]
        else:
            return None


class MyLibraryView(View):
    def get(self, request):
        user_books = UserBook.objects.filter(user=request.user)
        # Implement logic to categorize user's books into different shelves
        return render(request, "books/my_library.html", {"user_books": user_books})


# Add other views as needed (e.g., LoginView, RegisterView)
class SearchBooksView(View):
    template_name = "books/search_books.html"

    def get(self, request, *args, **kwargs):
        query = request.GET.get("query", "")
        order_by = request.GET.get("order_by", "relevance")  # Default to relevance

        # Implement logic to search books using Google Books API
        api_url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            # 'key': settings.GOOGLE_BOOKS_API_KEY,
            "q": query,
            "orderBy": order_by,
        }
        response = requests.get(api_url, params=params)
        data = response.json()
        books = data.get("items", [])

        context = {
            "query": query,
            "order_by": order_by,
            "books": books,
        }

        return render(request, self.template_name, context)


class LatestBooksView(View):
    def get(self, request, *args, **kwargs):
        # Fetch latest books using Google Books API
        api_url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            # 'key': settings.GOOGLE_BOOKS_API_KEY,
            "q": "subject:fiction",
            "maxResults": 10,
            "orderBy": "newest",
        }
        response = requests.get(api_url, params=params)
        data = response.json()
        latest_books = data.get("items", [])

        context = {"latest_books": latest_books}
        return render(request, "books/latest_books.html", context)


class PopularBooksView(View):
    def get(self, request, *args, **kwargs):
        # Fetch popular books using NYT Best Sellers API
        nyt_api_key = settings.NYT_API_KEY
        api_url = "https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json"
        params = {"api-key": nyt_api_key}
        response = requests.get(api_url, params=params)
        data = response.json()
        popular_books = data.get("results", {}).get("books", [])

        context = {"popular_books": popular_books}
        return render(request, "books/popular_books.html", context)


class ForYouBooksView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        # Fetch personalized recommendations for the user based on their activity
        # You need to implement your recommendation logic, for now, let's fetch some random books
        api_url = "https://www.googleapis.com/books/v1/volumes"
        params = {
            # 'key': settings.GOOGLE_BOOKS_API_KEY,
            "maxResults": 20,
            "orderBy": "relevance",
        }
        response = requests.get(api_url, params=params)
        data = response.json()
        personalized_books = data.get("items", [])

        context = {"personalized_books": personalized_books}
        return render(request, "books/for_you_books.html", context)
