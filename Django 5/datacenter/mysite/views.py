from django.shortcuts import render
from django.http import HttpResponse
from .scrapers import CDC

def home(request):
    
    return render(request, 'home/home.html')

def about(request):
    
    return render(request, 'about/about.html')

def spider(request):
 
    CDCinfor = CDC(request.POST.get("test"))
 
    context = {
        "disease": CDCinfor.scrape()
    }
 
    return render(request, "spider/spider.html", context)