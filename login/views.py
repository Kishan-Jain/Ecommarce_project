from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterAuthPage, forgetpswdForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def register(request):
    if request.method == 'POST':
        print("method post")
        fm = RegisterAuthPage(request.POST)
        if fm.is_valid():
            print("valid")
            fm.save()
            print('data feeded')
        
    else:
        fm = RegisterAuthPage()
    return render(request, "register.html", {'RegisterFormData' : fm}  )


def login(request):
    if request.user.is_authenticated:
        return redirect('')
    else:
        if request.method == 'POST':
            fm = LoginForm(request = request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                print("data pass")
                user = authenticate(username = uname, password = upass)
                
                if user is not None:
                    login(request, user)
               
                return redirect('')   
        else:
            fm = LoginForm()
        return render(request, 'login.html', {'loginform' : fm})
    



def forgetPsw(request):
    fm = forgetpswdForm()
    return render(request, "forgetPassword.html",{'forgetpswd' : fm})


