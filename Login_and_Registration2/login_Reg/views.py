from genericpath import exists
from django.shortcuts import render,redirect
from django.db import models
from .models import *
from . import models
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,'index.html')

def regiser(request):
    errors = User.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
    
        # redirect the user back to the form to fix the errors
    else:
        # if the errors object is empty, that means there were no errors!
            # include some logic to validate user input before adding them to the database!
        password = request.POST['passward']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  # create the hash    
        print(pw_hash)      # prints something like b'$2b$12$sqjyok5RQccl9S6eFLhEPuaRaJCcH3Esl2RWLm/cimMIEnhnLb7iC' 
        User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=pw_hash,

    )
    return redirect('/')

def login(request ):

    errors=User.objects.log_validator(request.POST)
            # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
    else:
        email=request.POST['email_log']
        object_user=User.objects.get(email=email)
        if not User.objects.filter(email=email).exists():
            return redirect('/')
            # return render(request,'success.html')
           # see if the username provided exists in the database
        user = User.objects.filter(email=request.POST['email_log']) # why are we using filter here instead of get?
        if user: # note that we take advantage of truthiness here: an empty list will return false
            logged_user = user[0] 
        # assuming we only have one user with this username, the user would be first in the list we get back
        # of course, we should have some logic to prevent duplicates of usernames when we create users
        # use bcrypt's check_password_hash method, passing the hash from our database and the password from the form
        if bcrypt.checkpw(request.POST['Passward_log'].encode(), logged_user.password.encode()):
            # if we get True after checking the password, we may put the user id in session
            request.session['userid'] = logged_user.id
            # never render on a post, always redirect!
            return render(request,'success.html')
    # if we didn't find anything in the database by searching by username or if the passwords don't match, 
    # redirect back to a safe route
    return redirect('/')

    # return render(request,'success.html')

def logout(request):
    return redirect('/')


    