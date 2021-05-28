from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return render(request, 'lobby.html')

def test(request):
    
    return render(request, 'test.html')

def test1(request):

    return render(request, '新文字文件.html')