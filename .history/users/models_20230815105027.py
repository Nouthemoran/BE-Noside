from django.db import models
from django.contrib.auth.models import AbstractUser,  UserManager
# Create your models here.

class User(AbstractUser):
name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Password field should not be stored in plaintext
    password = models.CharField(max_length=128)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
