from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

# Create your models here.
class Conference (models.Model):
    confId = models.CharField(max_length=255, primary_key= True)
    confName = models.CharField(max_length=255)
    detailConf = models.CharField(max_length=255)
    confImages = models.ImageField(upload_to='conference_images')
    

    def __str__(self):
        return self.confName
    
@receiver(pre_delete, sender=Conference)
def delete_conference_images(sender, instance, **kwargs):
    # Delete the associated images when a Conference instance is deleted
    if instance.confImages:
        # Get the path to the image file
        image_path = instance.confImages.path
        # Delete the file from the media directory
        os.remove(image_path)

    

