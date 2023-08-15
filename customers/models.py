from django.db import models

# Create your models here.


class Customer (models.Model):
    STATUS_CHOICES = [
        ('Lunas', 'Lunas'),
        ('Belum Lunas', 'Belum Lunas'),
    ]
     
    custId = models.CharField(max_length=255, primary_key= True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phoneNumber = models.CharField(max_length=255)
    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES, default='Belum Lunas')
    
    def __str__(self):
        return self.name