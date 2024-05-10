from django.shortcuts import render, redirect
from .models import offer_nav
from .models import categories
# Create your views here.


def home(request):
    
    offersData = offer_nav.objects.all()
    categoriesData = categories.objects.all()
    data = {
        'offersData' : offersData,
        'categoriesData' : categoriesData
    }

    return render(request, "index.html", data)

def numDetails(request, slug):
    numsDetails = categories.objects.get(links = slug )
    data = {
        'numsDetails' : numsDetails,
    }
    
    return render(request, "fashion.html", data)

