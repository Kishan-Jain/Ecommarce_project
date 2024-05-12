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

    try:
        
        name= request.POST.get("username")
        passw = request.POST.ger("password")

        logindata = {
            "username": name,
            "password": passw
        }
        return render(request, "index.html", data, logindata)
    except:
        pass
    
    try:
        
        email = request.POST.get("regemail")
        name= request.POST.get("username")
        passw = request.POST.ger("password")

        logindata = {
            "username": name,
            "password": passw
        }
        return render(request, "index.html", data, logindata)
    except:
        pass
     
    return render(request, "index.html", data)

def numDetails(request, slug):
    numsDetails = categories.objects.get(links = slug )
    
    data = {
        'numsDetails' : numsDetails,
        
    }
    
    categoriesData = categories.objects.all()
    
    if slug == "fashion":
        fashionitem = fashion.objects.all()
    
        data = {
            'categoriesData' : categoriesData,
            'numsDetails' : numsDetails,
            'fashionitem' : fashionitem
        }
        return render(request, "cat_base_page.html", data)
    
    
    return render(request, "cat_base_page.html", data)

def fashionData(request):
    fashionitem = fashion.objects.all()
    
    data = {
        'fashionitem' : fashionitem
    }
    
    return render(request, "cat_base_page.html", data)