from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class loginForm(forms.Form):
    userName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter User Id', 'class': 'form-control col-md-11'}))
    pswd = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder': 'Enter Password' ,'class': 'form-control col-md-11'}))
    
class registerForm(forms.Form):
    firstName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter firstName' ,'class': 'form-control col-md-9', 'style' : 'display:inline'}))
    lastName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter LastName' ,'class': 'form-control col-md-9', 'style' : 'display:inline'}))
    emailId = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder': 'Enter Email Address' ,'class': 'form-control col-md-9', 'style' : 'display:inline'}))
    userName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter User Id', 'class': 'form-control col-md-9','style' : 'display:inline'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password' ,'class': 'form-control col-md-9', 'style' : 'display:inline'}))
    city = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter City' ,'class': 'form-control col-md-10', 'style' : 'display:inline'}))
    state = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter State' ,'class': 'form-control col-md-9', 'style' : 'display:inline'}))
    zipCode = forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder': 'Enter zip code' ,'class': 'form-control col-md-8', 'style' : 'display:inline'}))
    
class forgetpswdForm(forms.Form):
    firstName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter firstName' ,'class': 'form-control col-md-12',  }))
    lastName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter LastName' ,'class': 'form-control col-md-12',  }))
    emailId = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder': 'Enter Email Address' ,'class': 'form-control col-md-12',  }))
    userName = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter User Id', 'class': 'form-control col-md-12', }))
    city = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter City' ,'class': 'form-control col-md-12',  }))
    state = forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Enter State' ,'class': 'form-control col-md-12',  }))
    zipCode = forms.IntegerField(widget= forms.NumberInput(attrs={'placeholder': 'Enter zip code' ,'class': 'form-control col-md-12',  }))


class PasswordForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password' ,'class': 'form-control col-md-9', 'style' : 'display:inline'})),
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Re-Enter Password' ,'class': 'form-control col-md-9', 'style' : 'display:inline'})),
    
class RegisterAuthPage(UserCreationForm):
   
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password' ,'class': 'form-control col-md-9', 'style' : 'display:inline'})),
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Re-Enter Password' ,'class': 'form-control col-md-9', 'style' : 'display:inline'})),
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter City' ,'class': 'form-control col-md-10', 'style' : 'display:inline'})),
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter State' ,'class': 'form-control col-md-9', 'style' : 'display:inline'})),
    zip_code =forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter zip code' ,'class': 'form-control col-md-8', 'style' : 'display:inline'})),
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email', 'username', 'date_joined']
        # total fields :- password, re-enter password, city, state, 
        widgets = {
            "first_name" : forms.TextInput(attrs={'placeholder': 'Enter firstName' ,'class': 'form-control col-md-9', 'style' : 'display:inline'}),
            "last_name" : forms.TextInput(attrs={'placeholder': 'Enter LastName' ,'class': 'form-control col-md-9', 'style' : 'display:inline'}),
            "email" : forms.EmailInput(attrs={'placeholder': 'Enter Email Address' ,'class': 'form-control col-md-9', 'style' : 'display:inline'}),
            'username' : forms.TextInput(attrs={'placeholder': 'Enter User Id', 'class': 'form-control col-md-9','style' : 'display:inline'}),
            
        }
           
