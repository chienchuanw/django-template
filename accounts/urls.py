from django.urls import path
from . import views
from .views import UserRegisterView

app_name = "accounts"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", views.login, name="login"),
]
