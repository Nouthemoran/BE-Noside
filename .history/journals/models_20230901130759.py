from django.db import models

# Create your models here.
class Journal (models.Model):
    jurnalId = models.CharField(max_length=255, primary_key= True)
    jurnalName = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    detailJurnal = models.CharField(max_length=255)
    jurnalImages = models.ImageField(upload_to='/', null=True, blank=True)
    
    def __str__(self):
        return self.jurnalImages
    
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