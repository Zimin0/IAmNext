from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    def __str__(self):
        return f"Профиль \"{self.user.username}\""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="media", blank=True, null=True)
