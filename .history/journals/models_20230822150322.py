from django.db import models

# Create your models here.
class Journal (models.Model):
    jurnalId = models.CharField(max_length=255, primary_key= True)
    jurnalName = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    detailJurnal = models.CharField(max_length=255)
    jurnalImages = models.CharField(max_length=255)
    
    def __str__(self):
        return self.jurnalImages