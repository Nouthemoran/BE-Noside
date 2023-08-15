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
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Password field should not be stored in plaintext
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=30, unique=True, default="default_username")  # Default value added

    # Use the default UserManager
    objects = UserManager()

    # Make sure to call parent class constructor
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
    # REQUIRED_FIELDS should include any required fields for user creation
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
