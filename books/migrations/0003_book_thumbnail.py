# Generated by Django 4.2.7 on 2024-01-10 23:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0002_remove_book_cover_link_remove_book_cover_thumbnail_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="thumbnail",
            field=models.URLField(blank=True, null=True),
        ),
    ]
