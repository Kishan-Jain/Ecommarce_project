from django.contrib import admin
from . import models

# Register your models here.

class LoginData_admin(admin.ModelAdmin):
    list_display = ("fristname", 'lastname', 'userId', '')