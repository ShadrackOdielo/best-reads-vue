# Generated by Django 4.2.7 on 2024-01-15 14:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0004_userbook_remove_bookauthor_author_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="google_books_id",
            new_name="isbn",
        ),
    ]
