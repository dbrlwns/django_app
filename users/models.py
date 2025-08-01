from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        "프로필 이미지",
        upload_to="users/profile",
        blank=True,
    )
