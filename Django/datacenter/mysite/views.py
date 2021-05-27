from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    
    return render(request, 'lobby.html')

def test(request):
    
    return render(request, 'test.html')
