from django.db import models

# Create your models here.

class KirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=15,  unique=True)
    update = models.DateTimeField(auto_now=True) #everytime the model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model whas created
    

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)