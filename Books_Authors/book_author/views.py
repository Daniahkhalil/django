from shutil import register_unpack_format
from sys import modules
from django.shortcuts import render ,redirect
from django.db import models
from .models import *
from . import models

# Create your views here.

def index(request):
    list_of_all_Books=models.list_of_Books()

    context={

        "list_of_books":list_of_all_Books,

    }
    return render(request,'index.html',context)

def adding_book(request):
    book.objects.create(title=request.POST['title'],desc=request.POST['description'])
    return redirect('/')

def view_book(request,id):
    object_book=book.objects.get(id=id)
    list_of_authors=object_book.authors.all()
    context={
        "book":object_book,
        "list_of_authors":list_of_authors,
        "authors":authors.objects.all(),
    }
    return render(request,'book_details.html',context)


def adding_author(request,id):
    object_book=book.objects.get(id=id)
    print(object_book)
    object_author=authors.objects.get(id = request.POST['author_name'])
    object_book.authors.add(object_author)
    return redirect(f'/books/{object_book.id}')


def view_authors(request):
    list_of_all_authors=models.list_of_authors()

    context={

        "list_of_authors":list_of_all_authors,

    }
    return render(request,'authors.html',context)

def view_book(request,id):
    object_author=authors.objects.get(id=id)
    list_of_books=object_author.books.all()
    context={
        "author":object_author,
        "list_of_books":list_of_books,
        "books":book.objects.all(),
    }
    return render(request,'authors_details.html',context)

def adding_author2(request):
    book.objects.create(first_name=request.POST['first_name'],lat_name=request.POST['last_name'],note=request.POST['notes'])
    return redirect('author')

    

