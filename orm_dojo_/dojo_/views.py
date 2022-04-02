from ast import mod
from multiprocessing import context
from wsgiref.util import request_uri
from django.shortcuts import render,redirect
# from flask import redirect
from .models import *
from . import models

# Create your views here.
def index(request):
    list_of_dojos=models.list_of_all_dojos()
    print( list_of_dojos)
    
    # list_dojos_name=[]
    # for dojo in list_of_dojos:
    #     list_dojos_name.append(dojo.name)


    print(list_of_dojos)
    context={
        "list_of_dojos":list_of_dojos,

    }
    return render(request,'index.html',context)


def add_dojo(request):
    Dojo.objects.create(name=request.POST['dojo_name'],city=request.POST['dojo_city'],State=request.POST['dojo_state'])
    return redirect("/")

def add_ninja(request):
    # list_of_dojos=models.list_of_all_dojos()
    # for dojo in list_of_dojos:
    #     if dojo.name==request.POST['dojo_selected']:
    #         dojo_object= Dojo.objects.get(id=dojo.id)
    #         break
    dojo_object=Dojo.objects.get(id=int(request.POST['dojos_id']))
    print(dojo_object.dojos.all())
    for ninja in dojo_object.dojos.all():
        print(ninja.first_name)


    Ninja.objects.create(first_name=request.POST['ninja_name'],last_name=request.POST['Last_name'],dojo=dojo_object)
    # print(dojo_object)
    # print(request)
    # print(request.POST)
    # print(request.POST['dojos_id'])
    return redirect("/")