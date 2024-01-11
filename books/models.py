from django.conf import settings

# models for the books app for use while fetching book data from google books api and nyt books api
from django.db import models


class Book(models.Model):
    google_book_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    authors = models.JSONField(default=list)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    isbn_13 = models.CharField(max_length=13, blank=True, null=True)
    isbn_10 = models.CharField(max_length=10, blank=True, null=True)
    page_count = models.PositiveIntegerField(blank=True, null=True)
    print_type = models.CharField(max_length=20, blank=True, null=True)
    thumbnail = models.URLField(blank=True, null=True)
    categories = models.JSONField(default=list)
    maturity_rating = models.CharField(max_length=20, blank=True, null=True)
    image_links = models.JSONField(default=dict)
    language = models.CharField(max_length=10, blank=True, null=True)
    preview_link = models.URLField(blank=True, null=True)
    info_link = models.URLField(blank=True, null=True)
    canonical_volume_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @classmethod
    def create_from_api(cls, api_data):
        volume_info = api_data.get("volumeInfo", {})
        isbn_10 = next(
            (
                identifier.get("identifier", "")
                for identifier in volume_info.get("industryIdentifiers", [])
                if identifier.get("type") == "ISBN_10"
            ),
            "",
        )

        return cls(
            google_book_id=api_data.get("id", ""),
            title=volume_info.get("title", ""),
            subtitle=volume_info.get("subtitle", ""),
            authors=volume_info.get("authors", []),
            publisher=volume_info.get("publisher", ""),
            published_date=volume_info.get("publishedDate", None),
            description=volume_info.get("description", ""),
            isbn_13=volume_info.get("industryIdentifiers", [{}])[0].get("identifier", ""),
            isbn_10=isbn_10,
            page_count=volume_info.get("pageCount", None),
            print_type=volume_info.get("printType", ""),
            categories=volume_info.get("categories", []),
            maturity_rating=volume_info.get("maturityRating", ""),
            image_links=volume_info.get("imageLinks", {}),
            language=volume_info.get("language", ""),
            preview_link=volume_info.get("previewLink", ""),
            info_link=volume_info.get("infoLink", ""),
            canonical_volume_link=api_data.get("canonicalVolumeLink", ""),
        )


class Author(models.Model):
    """Model for the Author object"""

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # model for the category object from the google books api


class Category(models.Model):
    """Model for the Category object"""

    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # model for the book author object from the google books api


class BookAuthor(models.Model):
    """Model for the BookAuthor object"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} - {self.author.name}"

    # model for the book category object from the google books api


class BookCategory(models.Model):
    """Model for the BookCategory object"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} - {self.category.name}"

    # model for the book review object from the google books api


class BookReview(models.Model):
    """Model for the BookReview object"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} - {self.review}"

    # model for the book rating object from the google books api


class BookRating(models.Model):
    """Model for the BookRating object"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} - {self.rating}"

    # model for the book shelf object from the google books api


class BookShelf(models.Model):
    """Model for the BookShelf object"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    shelf = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} - {self.shelf}"

    # model for the book user object from the Google books api


class BookUser(models.Model):
    """Model for the BookUser object"""

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} - {self.user.username}"

    # model for the book user review object from the google books api


class BookUserReview(models.Model):
    """Model for the BookUserReview object"""

    book_user = models.ForeignKey(BookUser, on_delete=models.CASCADE)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book_user.book.title} - {self.book_user.user.username} - {self.review}"

    # model for the book user rating object from the google books api


class BookUserRating(models.Model):
    """Model for the BookUserRating object"""

    book_user = models.ForeignKey(BookUser, on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book_user.book.title} - {self.book_user.user.username} - {self.rating}"

    # model for the book user shelf object from the Google books api


class BookUserShelf(models.Model):
    """Model for the BookUserShelf object"""

    book_user = models.ForeignKey(BookUser, on_delete=models.CASCADE)
    shelf = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book_user.book.title} - {self.book_user.user.username} - {self.shelf}"

    # model for the book user status object from the google books api


class BookUserStatus(models.Model):
    """Model for the BookUserStatus object"""

    book_user = models.ForeignKey(BookUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    page = models.IntegerField()
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.finished:
            return (
                f"{self.book_user.book.title} - {self.book_user.user.username} "
                f"- {self.status} - {self.page} - Finished"
            )
        else:
            return f"{self.book_user.book.title} - {self.book_user.user.username} - {self.status} - {self.page}"

    # model for the book user status update object from the google books api
