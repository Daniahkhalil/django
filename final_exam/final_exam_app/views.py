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
            'user_name':request.session['user_name'],
            'user_id':request.session['logged_user_id'],
            'cars':Car.objects.all()
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

def display_cars(request):
    return redirect('/home')

def show_add(request):
    return render(request,'add_car.html')

def add_car(request):
    price=request.POST['price']
    model=request.POST['model']
    year=request.POST['year']
    desc=request.POST['desc']
    user_object=User.objects.get(id=request.session['logged_user_id'])
    car_object=Car.objects.create(price=price,model=model,year=year,desc=desc,seller=user_object)
    return redirect('/home')


def logout(request):
    request.session.flush()
    return redirect('/')