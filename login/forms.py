from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True, 'placeholder': 'Enter User Id', 'class': 'form-control col-md-11'}))
    password = forms.CharField(
        label="Password", 
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password' ,'class': 'form-control col-md-11'}),
    )
    
   
class forgetpswdForm(forms.Form):
    firstName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter firstName' ,'class': 'form-control col-md-12',  }))
    lastName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter LastName' ,'class': 'form-control col-md-12',  }))
    emailId = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder': 'Enter Email Address' ,'class': 'form-control col-md-12',  }))
    userName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter User Id', 'class': 'form-control col-md-12', }))
    



    
class RegisterAuthPage(UserCreationForm):
    password1 = forms.CharField(
            widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Enter Password' ,'class': 'form-control col-md-9'}),
        )
    password2 = forms.CharField(
            widget=forms.TextInput(attrs={"autocomplete": "new-password", 'placeholder': 'Enter Password(again)' ,'class': 'form-control col-md-9'}),
        )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'date_joined']
        # total fields :- password, re-enter password, city, state, 
        widgets = {
            "first_name" : forms.TextInput(attrs={'placeholder': 'Enter firstName' ,'class': 'form-control col-md-9 d-inline'}),
            "last_name" : forms.TextInput(attrs={'placeholder': 'Enter LastName' ,'class': 'form-control col-md-9 d-inline' }),
            "email" : forms.EmailInput(attrs={'placeholder': 'Enter Email Address' ,'class': 'form-control col-md-9 d-inline'}),
            'username' : forms.TextInput(attrs={'placeholder': 'Enter User Id', 'class': 'form-control col-md-9 d-inline'}),
            
        }
           
