from django.db import models
from django.contrib.auth.models import AbstractUser,  UserManager
# Create your models here.

# class User(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255)
#     username = None
#     objects = UserManager()

#     REQUIRED_FIELDS = []


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    email = models.EmailField(unique=True)
    # Password field should not be stored in plaintext
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=30, unique=True)  # Default value added

    # Use the default UserManager

    # Make sure to call parent class constructor

    # REQUIRED_FIELDS should include any required fields for user creation
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
    return self.username
