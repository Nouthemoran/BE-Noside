from django.db import models

# Create your models here.
class Repository (models.Model):
    STATUS_CHOICES = [
        ('kota', 'kota'),
        ('provinsi ', 'provinsi '),
        ('negara ', 'negara '),
    ]
     
    repoId = models.CharField(max_length=255, primary_key= True)
    repoName = models.CharField(max_length=255)
    address = models.CharField(
        max_length=255,
]
    
    def __str__(self):
        return self.repoName