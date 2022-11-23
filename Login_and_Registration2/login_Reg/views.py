from django.shortcuts import render, redirect, HttpResponse
from django.db import models
from .models import *
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
import bcrypt

def index(request):
    return render(request,'index.html')

def home_page(request):
    if 'logged_user_id' in request.session:
        context={
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
            if 'confirm_password' in request.POST:
                is_private = request.POST['confirm_password']
            else:
                is_private = False

            print(is_private)
            print('hellllo')
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
            print(pw_hash)    
            new_user=User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash)
            # if new_user is not None:
            #     if not request.session:
            new_user.save()
            request.session['logged_user_id']= new_user.id
            print(new_user.id)
            request.session['user_name']= new_user.first_name
            print(new_user.first_name)
            return HttpResponse("regiser succssfully")

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

def logout(request):
    request.session.flush()
    return redirect('/')