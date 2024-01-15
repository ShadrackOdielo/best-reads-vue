from django.urls import path

from .views import (
    BookDetailView,
    ForYouBooksView,
    HomePageView,
    LatestBooksView,
    MyLibraryView,
    PopularBooksView,
    SearchBooksView,
)

app_name = "books"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("book/<str:isbn>/", BookDetailView.as_view(), name="book_detail"),
    path("my-library/", MyLibraryView.as_view(), name="my_library"),
    path("search/", SearchBooksView.as_view(), name="search_books"),
    # Add other URLs for authentication, registration, etc.
    path("latest_books/", LatestBooksView.as_view(), name="latest_books"),
    path("popular_books/", PopularBooksView.as_view(), name="popular_books"),
    path("for_you_books/", ForYouBooksView.as_view(), name="for_you_books"),
]
