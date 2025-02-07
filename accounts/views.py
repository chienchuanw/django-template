from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


def register(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/register.html")


class UserRegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/login.html")
