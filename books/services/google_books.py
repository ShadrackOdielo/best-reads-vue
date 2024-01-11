# books/services/google_books.py
import os

import requests

from books.models import Author, Book, BookReview, Category

# api key for the Google books api from the .env file and base url for the api
API_KEY = os.environ.get("GOOGLE_BOOKS_API_KEY")
BASE_URL = "https://www.googleapis.com/books/v1/volumes"


# fetch data from the Google Books API and map it to our Book model
def search_books(query):
    """Search for books using the Google Books API.

    Args:
        query (str): Search query.

    Returns:
        list: List of Book objects.

    """
    params = {"q": query, "key": API_KEY}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    books = []
    for api_book in data["items"]:
        books.append(_map_to_book_model(api_book))
    return books


def _map_to_book_model(api_data):
    """Map data from Google Books API to Book model.

    Args:
        api_data (dict): Data from Google Books API.

    Returns:
        Book: Book model instance.

    """
    api_data = api_data["volumeInfo"]
    return Book(
        title=api_data.get("title", ""),
        subtitle=api_data.get("subtitle", ""),
        description=api_data.get("description", ""),
        published_date=api_data.get("publishedDate", ""),
        page_count=api_data.get("pageCount", 0),
        thumbnail=api_data.get("imageLinks", {}).get("thumbnail", ""),
        language=api_data.get("language", ""),
        preview_link=api_data.get("previewLink", ""),
        canonical_volume_link=api_data.get("canonicalVolumeLink", ""),
    )


def get_book(book_id):
    """Get book by id.

    Args:
        book_id (str): Book id.

    Returns:
        Book: Book model instance.

    """
    params = {"key": API_KEY}
    response = requests.get(f"{BASE_URL}/{book_id}", params=params)
    response.raise_for_status()
    api_data = response.json()
    return _map_to_book_model(api_data)


# get latest books from google books api
def get_latest_books():
    """Get latest books from Google Books API.

    Returns:
        list: List of Book objects.

    """
    params = {"q": "subject:fiction", "orderBy": "newest", "key": API_KEY}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    books = []
    for api_book in data["items"]:
        books.append(_map_to_book_model(api_book))
    return books


# get popular books from google books api
@staticmethod
def get_popular_books():
    """most popular fiction books from Google Books API.

    Returns:
        list: List of Book objects.

    """
    params = {"q": "subject:fiction", "orderBy": "relevance", "key": API_KEY}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    books = []
    for api_book in data["items"]:
        books.append(_map_to_book_model(api_book))
    return books


# get books for you from Google books api
def get_books_for_you():
    """Get recommendations from Google Books API.

    Returns:
        list: List of Book objects.

    """
    params = {"q": "subject:fiction", "orderBy": "relevance", "key": API_KEY}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    books = []
    for api_book in data["items"]:
        books.append(_map_to_book_model(api_book))
    return books


# get book authors from Google books api
@staticmethod
def get_book_authors(book_id):
    """Get book authors from Google Books API.

    Args:
        book_id (str): Book id.

    Returns:
        list: List of Author objects.

    """
    params = {"key": API_KEY}
    response = requests.get(f"{BASE_URL}/{book_id}", params=params)
    response.raise_for_status()
    api_data = response.json()
    authors = []
    for api_author in api_data["volumeInfo"]["authors"]:
        authors.append(Author(name=api_author))
    return authors


# get book categories from Google books api


@staticmethod
def get_book_categories(book_id):
    """Get book categories from Google Books API.

    Args:
        book_id (str): Book id.

    Returns:
        list: List of Category objects.

    """
    params = {"key": API_KEY}
    response = requests.get(f"{BASE_URL}/{book_id}", params=params)
    response.raise_for_status()
    api_data = response.json()
    categories = []
    for api_category in api_data["volumeInfo"]["categories"]:
        categories.append(Category(name=api_category))
    return categories


# get book reviews from Google books api


@staticmethod
def get_book_reviews(book_id):
    """Get book reviews from Google Books API.

    Args:
        book_id (str): Book id.

    Returns:
        list: List of BookReview objects.

    """
    params = {"key": API_KEY}
    response = requests.get(f"{BASE_URL}/{book_id}", params=params)
    response.raise_for_status()
    api_data = response.json()
    reviews = []
    for api_review in api_data["volumeInfo"]["reviews"]:
        reviews.append(BookReview(review=api_review))
    return reviews
