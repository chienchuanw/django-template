from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User


def register(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/register.html")


class UserRegisterView(FormView):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        user = form.save()

        # Assign specific backend validation from AUTHENTICATION_BACKENDS in settings.py
        user.backend = "django.contrib.auth.backends.ModelBackend"

        # Auto-login after register successfully
        login(self.request, user, backend=user.backend)
        return redirect(self.get_success_url())

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        return super().dispatch(request, *args, **kwargs)


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        # Remember account for 30 days
        remember_me = self.request.POST.get("remember_me")
        response = super().form_valid(form)

        # Default is 7 days which is set in SESSION_COOKIE_AGE in settings.py
        if remember_me:
            self.request.session.set_expiry(60 * 60 * 24 * 30)

        return response


class UserLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        return response


def profile(request):
    return render(request, "accounts/profile.html")


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        return context


class UserProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = "accounts/edit.html"
    model = User
    fields = ["email", "first_name", "last_name", "username"]
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        return self.request.user
