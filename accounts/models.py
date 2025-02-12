from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    # related_name allows reverse query from User model
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    mobile = models.CharField(max_length=20, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
