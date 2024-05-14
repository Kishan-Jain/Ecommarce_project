from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import LoginData
from .forms import loginForm, registerForm

# Create your views here.

def login(request):
    fm = loginForm()
    return render(request, "login.html", {'loginform' : fm})

def register(request):
    fm = registerForm()
    return render(request, "register.html", {'registerform' : fm}  )

def forgetPsw(request):
    fm = registerForm()
    return render(request, "forgetPassword.html",{'forgetpswd' : fm})


