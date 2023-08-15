from django.db import models

# Create your models here.
class Customer (models.Model):
    custId = models.CharField(max_length=255, primary_key= True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phoneN