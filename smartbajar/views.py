from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from homepage.models import offer_nav
from homepage.models import categories
def home(request):
    
    offersData = offer_nav.objects.all()
    categoriesData = categories.objects.all()
    data = {
        'offersData' : offersData,
        'categoriesData' : categoriesData
    }

    return render(request, "index.html", data)