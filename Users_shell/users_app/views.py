from django.shortcuts import render,redirect
from .models import *

def index(request):
    context = {
    	"user": User.objects.all()
    }
    return render(request, "index.html", context)

def insert(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],email=request.POST['email'],
    age=request.POST['age'])
    
    return redirect("/")