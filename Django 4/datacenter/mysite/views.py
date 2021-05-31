from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return render(request, 'home/home.html')

def about(request):
    
    return render(request, 'about/about.html')

def test(request):

    return render(request, 'test.html')