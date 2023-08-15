from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    email = models.EmailField(null=True)
    # Password field should not be stored in plaintext
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=30, unique=True)  # Default value added

    # Make sure to call parent class constructor
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
    # REQUIRED_FIELDS should include any required fields for user creation
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
