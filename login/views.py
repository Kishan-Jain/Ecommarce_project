from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import LoginData
from .forms import loginForm, registerForm, RegisterAuthPage, PasswordForm
from django.contrib.auth.forms import UserCreationForm




# Create your views here.


def password(request): 
    if request.method == 'POST':
        fm = PasswordForm(request.POST)
        if fm.is_valid:
            fm.save()
    else:
        fm = UserCreationForm()
        
    return render(request, "register2.html",{'form' : fm})

def register(request):
    if request.method == 'POST':
        fm = RegisterAuthPage(request.POST)
        if fm.is_valid():
            fm.save()
        else:
            fm = RegisterAuthPage()
    else:
            fm = RegisterAuthPage()
    return render(request, "register.html", {'RegisterFormData' : fm}  )


def login(request):
    fm = loginForm()
    return render(request, "login.html", {'loginform' : fm})



def forgetPsw(request):
    fm = registerForm()
    return render(request, "forgetPassword.html",{'forgetpswd' : fm})


