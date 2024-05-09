from django.db import models

# Create your models here.

class offer_nav(models.Model):
    offer_title = models.CharField(max_length=100)
    offer_disc = models.TextField(max_length=500, null=True, default=None)
    
class categories(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to="categaries/", default= None, null=True, blank=True)
    discription = models.TextField(max_length=500, null=True, default=None)