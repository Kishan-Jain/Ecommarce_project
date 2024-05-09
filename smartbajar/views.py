from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from homepage.models import offer_nav
def home(request):
    
    offersData = offer_nav.objects.all()
    print(offersData)
    data = {
        'offersData' : offersData
    }
    
    return render(request, "index.html", data)