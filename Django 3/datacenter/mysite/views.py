from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return render(request, 'home/home.html')

def aboutme(request):
    
    return render(request, 'aboutme/aboutme.html')

def test1(request):

    return render(request, '新文字文件.html')