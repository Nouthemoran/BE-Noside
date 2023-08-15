from django.db import models

# Create your models here.
class StatusCustomer(models.TextChoices):
    LUNAS = 'Lunas', ('Lunas')
    BELUM_lUNAS = 'Belum Lunas', ('Belum Lunas')

class Customer (models.Model):
    custId = models.CharField(max_length=255, primary_key= True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    status = status = models.CharField(
        max_length=10,
        choices=StatusSekolah.choices)