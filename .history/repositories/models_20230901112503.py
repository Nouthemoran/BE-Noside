from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
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
        choices=STATUS_CHOICES)
    detailRepo = models.CharField(max_length=255)
    repoImages = models.ImageField(upload_to='repository_images/', null=True, blank=True)
    background = models.ImageField(upload_to='backgrounds/', null=True, blank=True)
    
    def __str__(self):
        return self.repoName
    
from django.db import models


@receiver(pre_delete, sender=Repository)
def delete_repository_images(sender, instance, **kwargs):
    # Delete the associated images when a Repository instance is deleted
    if instance.repoImages:
        # Get the path to the image file
        image_path = instance.repoImages.path
        # Delete the file from the media directory
        os.remove(image_path)

    if instance.background:
        # Get the path to the background image file
        background_path = instance.background.path
        # Delete the file from the media directory
        os.remove(background_path)