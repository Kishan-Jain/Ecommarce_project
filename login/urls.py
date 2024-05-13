from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginform, name='login'),
    path('register/', views.registerform, name='register'),
    path('forget-password/', views.forgetPsw, name='forgetPsw'),
    
    
]
