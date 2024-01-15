from datetime import datetime

import requests

from .models import Book


def fetch_google_books_data(isbn):
    api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}"
    response = requests.get(api_url)
    data = response.json()

    if "items" in data:
        book_data = data["items"][0]["volumeInfo"]

        # Use ISBN as the unique identifier
        isbn = book_data.get("industryIdentifiers", [{}])[0].get("identifier", "")
        published_date_str = book_data.get("publishedDate", "")

        # Check if the date contains only the year
        if len(published_date_str) == 4:
            # If it's just a year, set the date to January 1 of that year
            try:
                published_date = datetime.strptime(published_date_str, "%Y").date()
            except ValueError:
                published_date = None
        else:
            # Otherwise, try to format it as YYYY-MM-DD
            try:
                published_date = datetime.strptime(published_date_str, "%Y-%m-%d").date()
            except ValueError:
                published_date = None

        # Now, you can use this ISBN in your Book model
        book, created = Book.objects.get_or_create(
            isbn=isbn,
            defaults={
                "title": book_data.get("title", ""),
                "authors": ", ".join(book_data.get("authors", [])),
                "description": book_data.get("description", ""),
                "published_date": published_date,
                "categories": ", ".join(book_data.get("categories", [])),
                "average_rating": book_data.get("averageRating", None),
                "thumbnail_url": book_data.get("imageLinks", {}).get("thumbnail", ""),
                # other fields...
            },
        )

        return book_data
    else:
        return None
