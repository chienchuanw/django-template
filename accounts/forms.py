from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "register-input"})
    )
    email = forms.EmailField(
        required=True,
        label="Email",
        help_text="Please enter valid email address",
        widget=forms.EmailInput(attrs={"class": "register-input"}),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "register-input"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "register-input"})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()

        return user
