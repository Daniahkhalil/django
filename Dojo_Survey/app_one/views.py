
from django.shortcuts import render, HttpResponse,redirect 


def index(request):
    return render(request,'index.html')

def show(request):
    name=request.POST['yourname']
    location=request.POST['location']
    fav=request.POST['fav']
    free=request.POST['free']
    
    context={
        "name":name,
        "location" :location,
        "fav":fav,
        "free" :free
    }
    return render(request,"show.html",context)