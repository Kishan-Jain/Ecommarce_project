from django.db import models

# Create your models here.

class LoginData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50, null=True, blank=True)
    emailId = models.EmailField()
    userName = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    address = models.TextField(max_length=200)
    
    