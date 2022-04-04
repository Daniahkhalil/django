from multiprocessing import context
from django.shortcuts import render,redirect

from .models import *
from . import models
from django.contrib import messages

# Create your views here.
def index(reuqest):
  show_list=models.list_of_shows()
  context = {
        "list_of_shows" : show_list,
    }
  return render(reuqest,'index.html',context)

def book_details(request,id):
    object_show=Show.objects.get(id=id)
    context = {
        "show" : object_show,
    }  
    return render(request,'show.html',context)

def show_edit(request,id):
    object_show=Show.objects.get(id=id)
    context={
        "show":object_show,
    }
    return render(request,'edit.html',context)

def updated(request,id):
    object_show=Show.objects.get(id=id)
    errors =Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/show/{object_show.id}/edit')
    
    else:
        object_show.title=request.POST['title']
        object_show.network=request.POST['network']
        object_show.release_date=request.POST['release date']
        object_show.save()
      
    # context={
    #     "tilte":object_show.title,
    #     "newtwork":object_show.network,
    #     "release_date":object_show.release_date,
    # }
    return redirect(f'/show/{object_show.id}')
    

    

def delete_show(request,id):
    object_show=Show.objects.get(id=id)
    object_show.delete()

    return redirect('/show')


def create_show(request):
    return render(request,'create.html')

def create(request):
    # print(Show.objects.basic_validator(request.POST))
    errors =Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)

    else:
        Show.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release date'])
    return redirect('/show/create')


def go_back(request):
    return redirect('/show')

# def show_go_back(request,id):

#     return redirect('/show')


