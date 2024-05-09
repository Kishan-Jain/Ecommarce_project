from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from homepage import models
def home(request):
    
    # offersData = navbar_offer.objects.all()
    # print(offersData)
    # data = {
    #     'offersData' : offersData
    # }
    
    return render(request, "index.html")