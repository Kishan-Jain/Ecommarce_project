from django import forms

class loginForm(forms.Form):
    userName = forms.CharField()
    pswd = forms.CharField()
    
class registerForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    emailId = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Enter Email Address', 'style': 'margin-left: 35px;  width: 78%;'}))
    userName = forms.CharField()
    password = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipCode = forms.IntegerField()
    
class forgetpswdForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    emailId = forms.EmailField()
    userName = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipCode = forms.IntegerField()
    