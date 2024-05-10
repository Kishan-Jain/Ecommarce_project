from django.shortcuts import render
from product import models
# Create your views here.

def cat_base_page(request):
    
    
    return render(request, "cat_base_page.html")

