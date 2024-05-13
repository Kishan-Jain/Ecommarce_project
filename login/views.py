from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import LoginData

# Create your views here.

def loginform(request):
    
    return render(request, "login.html")

def registerform(request):
    
    return render(request, "register.html")

def forgetPsw(request):
    
    return render(request, "forgetPassword.html")