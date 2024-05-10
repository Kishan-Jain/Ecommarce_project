from django.shortcuts import render, redirect
from .models import offer_nav, categories
from product.models import fashion

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
    fashionitem = fashion.objects.all()
    data = {
        'numsDetails' : numsDetails,
        'fashionitem' : fashionitem
    }
    
    
    return render(request, "cat_base_page.html", data)

