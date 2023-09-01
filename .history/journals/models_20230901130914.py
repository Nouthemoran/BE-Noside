from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

# Create your models here.
class Journal (models.Model):
    jurnalId = models.CharField(max_length=255, primary_key= True)
    jurnalName = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    detailJurnal = models.CharField(max_length=255)
    jurnalImages = models.ImageField(upload_to='journal_images/', null=True, blank=True)
    
    def __str__(self):
        return self.jurnalImages
    
@receiver(pre_delete, sender=Journal)
def delete_repository_images(sender, instance, **kwargs):
    # Delete the associated images when a Journal instance is deleted
    if instance.jurn:
        # Get the path to the image file
        image_path = instance.jurn.path
        # Delete the file from the media directory
        os.remove(image_path)

    if instance.background:
        # Get the path to the background image file
        background_path = instance.background.path
        # Delete the file from the media directory
        os.remove(background_path)