from django.db import models

# Create your models here.
class Conference (models.Model):
    confId = models.CharField(max_length=255, primary_key= True)
    confName = models.CharField(max_length=255)
    detailConf = models.CharField(max_length=255)
    confImages = models.CharField(max_length=255)
    

    def __str__(self):
        return self.confName
    
    
    

