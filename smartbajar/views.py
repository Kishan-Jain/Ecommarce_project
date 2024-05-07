from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

def homepage(request):
    return render(request, "index.html")