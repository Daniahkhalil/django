from mmap import PAGESIZE
from unicodedata import name
from django.shortcuts import render, redirect
from django.db import models
from .models import *
from django.contrib import messages
import bcrypt
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.loader import render_to_string

# importing the necessary libraries
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from django.http import HttpResponse
from django.views.generic import View

 
from django.http import HttpResponse
from django.views.generic import View
 
#importing get_template from loader
from django.template.loader import get_template
 
# #import render_to_pdf from util.py 
# from .utils import render_to_pdf 



# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def reg(request):
    return render(request,'registration.html')

def register(request):
    print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
            print(pw_hash)    
            new_user=User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash)
            # if new_user is not None:
            #     if not request.session:
            # request.session['logged_user_id']= new_user.id
            print(new_user.id)
            # request.session['user_name']= new_user.first_name
            print(new_user.first_name)
            return redirect('/home')

def login(request ):
    print('hiiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
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


def cheque(request):
    return render(request,'cheque.html')

def draft(request):
    return render(request,'draft.html')

def addcheque(request):
    if request.method == "POST":
        errors = Cheque.objects.cheque_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                print('hiiiiii')
                messages.error(request, value)
            return redirect('/home/cheque')
        else:
            print('hi im cheque')
            name = request.POST['name']
            chequedate = request.POST['chequedate']
            returneddate= request.POST['returneddate']
            chequenumber = request.POST['chequenumber']
            chequeprice = request.POST['price']
            chequestatus = request.POST['status']
            bankname = request.POST['bankname']
            branchname = request.POST['branchname']
            Cheque_object=Cheque.objects.create(chequename=name,chequedate=chequedate,returneddate=returneddate,chequenumber=chequenumber,
            chequeprice=chequeprice,chequestatus=chequestatus,bankname=bankname,branchname=branchname)
            return redirect("/home")

def adddraft(request):
    
    if request.method == "POST":
        errors = Bill.objects.bill_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                print('hiiiiii Eroooor')
                messages.error(request, value)
            return redirect('/home/draft')
        else:
            print('hi im bill')
            draftname = request.POST['draftname']
            draftdate = request.POST['draftdate']
            draftnumber= request.POST['draftnumber']
            draftprice = request.POST['draftprice']
            draftstatus = request.POST['draftstatus']
            Bill_object=Bill.objects.create(billame=draftname,billdate=draftdate,billnumber=draftnumber,
            billprice=draftprice,billstatus=draftstatus)
            return redirect("/home")

def edit_cehque(request,id):
    print(id)
    cheque_object=Cheque.objects.get(id=id)
    context={
        'cheque':cheque_object
    }

    return render(request,'edit_cheque.html',context)

def update_my_cheque(request,id):
    name = request.POST['name']
    chequedate = request.POST['chequedate']
    returneddate= request.POST['returneddate']
    chequenumber = request.POST['chequenumber']
    chequeprice = request.POST['price']
    chequestatus = request.POST['status']
    bankname = request.POST['bankname']
    branchname = request.POST['branchname']
    cheque_object=Cheque.objects.get(id=id)
    cheque_object.chequename=name
    cheque_object.chequedate=chequedate
    cheque_object.returneddate=returneddate
    cheque_object.chequenumber=chequenumber
    cheque_object.chequeprice=chequeprice
    cheque_object.chequestatus=chequestatus
    cheque_object.bankname=bankname
    cheque_object.branchname=branchname
    cheque_object.save()
    return redirect('/home/display_cheque')


def dispaly_cheque(request):
    print(id)
    cheques=Cheque.objects.all()
    context={
        'cheques':cheques
    }
    return render(request,'cheque_report.html', context)

def delete_my_cheque(request,id):
    cheque_object=Cheque.objects.get(id=id)
    cheque_object.delete()
    return redirect('/home/display_cheque')

def edit_draft(request,id):
    print(id)
    draft_object=Bill.objects.get(id=id)
    context={
        'draft':draft_object
    }

    return render(request,'edit_draft.html',context)

def update_my_draft(request,id):
    draftname = request.POST['draftname']
    draftdate = request.POST['draftdate']
    draftnumber= request.POST['draftnumber']
    draftprice = request.POST['draftprice']
    draftstatus = request.POST['draftstatus']
    draft_object=Bill.objects.get(id=id)
    draft_object.billame=draftname
    draft_object.billdate=draftdate
    draft_object.billnumber=draftnumber
    draft_object.billprice=draftprice
    draft_object.billstatus=draftstatus
    draft_object.save()
    return redirect('/home/display_draft')


def dispaly_draft(request):
    print(id)
    drafts=Bill.objects.all()
    context={
        'drafts':drafts
    }
    return render(request,'draft_report.html', context)

def delete_my_draft(request,id):
    draft_object=Bill.objects.get(id=id)
    draft_object.delete()
    return redirect('/home/display_draft')

def logout(request):
    request.session.flush()
    return redirect('/')




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
