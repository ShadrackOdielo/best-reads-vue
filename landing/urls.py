from django.urls import path

from . import views

app_name = "landing"
urlpatterns = [
    path("", views.home, name="home"),
    path("description/", views.description, name="description"),
    path("about/", views.about_me, name="about_me"),
    path("contacts/", views.contacts, name="contacts"),
]
