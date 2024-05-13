from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

# Create your models here.

class Offer_Nav(models.Model):
    offer_title = models.CharField(max_length=100)
    offer_disc = models.TextField(max_length=500, null=True, default=" ")
    
    
class Categories(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(upload_to="pics/categaries/", default= " ", null=True, blank=True)
    disc = models.TextField(max_length=100, default=" ")
    links = AutoSlugField(populate_from = "title", unique=True, null=True, default="")
    
    
