from django.shortcuts import render
from django.http import HttpResponse
from .scrapers import CDC
from .test import test123
from .water import water

def home(request):
    
    return render(request, 'home/home.html')

def about(request):
    
    return render(request, 'about/about.html')

def spidercovid(request):
 
    CDCinfor = CDC(request.POST.get("test"))
 
    context = {
        "disease": CDCinfor.scrape()
    }
 
    return render(request, "spidercovid-19/spidercovid-19.html", context)

def spiderwater(request):
 
    waterinfor = water(request.POST.get("water"))
 
    infor = {
        "dam": waterinfor.scrape()
    }
 
    return render(request, "spiderwater/spiderwater.html", infor)

def test(request):
 
    testinfor = test123(request.POST.get("123"))
 
    test456 = {
        "apple": testinfor.scrape()
    }
 
    return render(request, "test.html", test456)
