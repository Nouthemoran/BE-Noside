from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    userpassword = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


    REQUIRED_FIELDS = []
