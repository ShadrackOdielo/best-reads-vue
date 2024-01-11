from django.shortcuts import render


def home(request):
    return render(request, "landing/home.html")


def description(request):
    return render(request, "landing/description.html")


def about_me(request):
    return render(request, "landing/about_me.html")


def contacts(request):
    return render(request, "landing/contacts.html")
