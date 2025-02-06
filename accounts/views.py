from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def register(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/register.html")


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/login.html")
