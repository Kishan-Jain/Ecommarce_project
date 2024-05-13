from django.shortcuts import render, redirect
from .models import Offer_Nav, Categories
from product.models import Fashion
# from product.models import antiqe, buety_product, daily_uses, divices, fashion, gerociry, kitchen_goods, leptop ,luxury, mobiles, stationary

# Create your views here.


# def cat_base_page(request):
#     antiqeitem =antiqe.objects.all()
#     buety_productitem = buety_product.objects.all()
#     daily_usesitem = daily_uses.objects.all()
#     divicesitem = divices.objects.all()
#     fashionitem = fashion.objects.all()
#     gerociryitem = gerociry.objects.all()
#     kitchen_goodsitem = kitchen_goods.objects.all()
#     leptopitem = leptop.objects.all() 
#     luxuryitem = luxury.objects.all()
#     mobilesitem = mobiles.objects.all()
#     stationaryitem = stationary.objects.all()

#     data = {
#         'antiqeitem' : antiqeitem,
#         'buety_productitem' : buety_productitem,
#         'daily_usesitem' : daily_usesitem,
#         'divicesitem' : divicesitem,
#         'fashionitem' : fashionitem,
#         'gerociryitem' : gerociryitem,
#         'kitchen_goodsitem': kitchen_goodsitem,
#         'leptopitem' : leptopitem,
#         'luxuryitem' : luxuryitem,
#         'mobilesitem' : mobilesitem,
#         'stationaryitem' : stationaryitem,

#     }
     
#     return render(request, "cat_base_page.html", data)




def home(request):

    offersData = Offer_Nav.objects.all()
    categoriesData = Categories.objects.all()
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
        username= request.POST.get("regusername")
        password = request.POST.ger("regpassword")

        logindata = {
            "email" : email,
            "username": username,
            "password": password,
        }
        return render(request, "index.html", data, logindata)
    except:
        pass
     
    return render(request, "index.html", data)

def numDetails(request, slug):
    categoryName = Categories.objects.get(links = slug )
    categoriesData = Categories.objects.all()
    
    categoryTitle = {
        'categoryName' : categoryName,
        'categoriesData' : categoriesData,
    }
    
    
    
    if slug == "fashion":
        fashionitem = Fashion.objects.all()
    
        data = {
            'categoriesData' : categoriesData,
            'categoryName' : categoryName,
            'fashionitem' : fashionitem
        }
        return render(request, "cat_base_page.html", data)
    
    
    return render(request, "cat_base_page.html", categoryTitle)

def fashionData(request):
    fashionitem = Fashion.objects.all()
    
    data = {
        'fashionitem' : fashionitem
    }
    
    return render(request, "cat_base_page.html", data)


