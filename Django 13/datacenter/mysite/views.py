from django.shortcuts import render
from django.http import HttpResponse
from .scrapers import CDC
from .water import water
from .about import aboutme
from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):
    template_name = 'home.html'

def home(request):
    
    return render(request, 'home/home.html')

def about(request):
    
    aboutme1 = aboutme(request.POST.get("about"))
 
    context = {
        "aboutme": aboutme1.scrape()
    }
    
    return render(request, 'about/about.html', context)

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
    return render(request, "test.html")

def test123(request):
    print("前端資料: ", request.POST)
    print("file:", request.FILES)

    for item in request.FILES:
        obj = request.FILES.get(item)      # 獲取要寫入的檔案
        filename = obj.name            # 獲取檔名
        f = open(filename, 'wb')
        for line in obj.chunks():      # 分塊寫入
            f.write(line)
        f.close()

    return render(request, "test123.html")

def information1(request):
    return render(request, "information1/information1.html")