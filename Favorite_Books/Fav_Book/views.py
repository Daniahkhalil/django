from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from django.db import models
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'index.html')

def home_page(request):
    if 'logged_user_id' in request.session:


        context={
            'books':Book.objects.all(),
            'user_name':request.session['user_name'],
            'user_id':request.session['logged_user_id']
        }
        return render(request,'home_page.html',context)
    return redirect('/')

def register(request):
    print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['passward']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
            print(pw_hash)    
            new_user=User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash)
            # if new_user is not None:
            #     if not request.session:
            request.session['logged_user_id']= new_user.id
            print(new_user.id)
            request.session['user_name']= new_user.first_name
            print(new_user.first_name)
            return redirect('/home')

def login(request ):

    if request.method == 'POST':
        errors=User.objects.log_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            # email=request.POST['email_log']
            # object_user=User.objects.get(email=email)
            # if  User.objects.filter(email=email).exists():
            # return redirect('/')
            user = User.objects.filter(email=request.POST['email_log'])
            # print(user.id)
            if user: 
                logged_user = user[0] 
                if bcrypt.checkpw(request.POST['Passward_log'].encode(), logged_user.password.encode()):
                    request.session['logged_user_id'] = logged_user.id
                    request.session['user_name']=logged_user.first_name
                    return redirect('/home')
            return redirect('/')
    return redirect('/')

def add_book(request):
    if request.method == 'POST':
        errors=Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home')
        else:
            user_object=User.objects.get(id=request.session['logged_user_id'])
            Book.objects.create(title=request.POST['title'],desc=request.POST['desc'],uploaded_by=user_object)
    return redirect('/home')

def update_fav_book(request,id):
    return redirect(f'/update/{id}')

def update(request,id):
    print(id)
    user_id=request.session['logged_user_id']
    user_object=User.objects.get(id=user_id)
    book_object=Book.objects.get(id=id)
   
    context={
        'user':user_object,
        'book':book_object,
    }

    if book_object.uploaded_by.id == user_id:
        return render(request,'my_book.html',context)
  
    return render(request,'update_fav.html',context)

def adds_to_fav(request,id):
    print(id)
    user_id=request.session['logged_user_id']
    user_object=User.objects.get(id=user_id)
    book_object=Book.objects.get(id=id)
    book_object.users_who_liked.add(user_object)
    book_fav=book_object.users_who_liked.all()
    print(book_fav)

    return redirect(f'/update/{id}')

def update_my_book(request,id):
    book_object=Book.objects.get(id=id)
    book_object.desc=request.POST['desc']
    book_object.save()
    return redirect(f'/update/{id}')

def delete_my_book(request,id):
    book_object=Book.objects.get(id=id)
    book_object.delete()
    return redirect('/home')

def unfav(request,id):
    print(id)
    user_id=request.session['logged_user_id']
    user_object=User.objects.get(id=user_id)
    book_object=Book.objects.get(id=id)
    book_object.users_who_liked.remove(user_object)
    return redirect(f'/update/{id}')

def logout(request):
    request.session.flush()
    return redirect('/')