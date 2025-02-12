from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import UserProfile


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


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(required=True, label="Username")
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = UserProfile
        fields = ["mobile", "birthday"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields["username"].initial = user.username
            self.fields["email"].initial = user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
            profile.save()

        return profile
