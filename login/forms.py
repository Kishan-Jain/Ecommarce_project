from django import forms

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
    