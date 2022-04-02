
from django.shortcuts import render, redirect
import random
# import datetime


def index(request,amount=0,name=''):
    if not 'total_gold' in request.session :
        request.session['total_gold']=0

        context={
        'total_gold':0
        
        }
    else:
        request.session['total_gold']+=amount
        context={
            'total_gold' : request.session['total_gold'],
            'golds_earned' : "Earned {} Golds from the !"+name.format(amount),
        }

    return render(request,"index.html",context)

# def farm(request):
#     amount=random.randint(10,20)
#     request.session['sub_gold']+=amount
#     print(amount)
#     print(request.session['sub_gold'])
#     return redirect("/")

# def cave(request):
#     amount=random.randint(5,10)
#     request.session['sub_gold']+=amount
#     print(amount)
#     print(request.session['sub_gold'])
#     return redirect("/")

# def house(request):
#     amount=random.randint(2,5)
#     request.session['sub_gold']+=amount
#     print(amount)
#     print(request.session['sub_gold'])
#     return redirect("/")

# def casino(request):
#     amount=random.randint(-50,50)
#     request.session['sub_gold']+=amount
#     print(amount)
#     print(request.session['sub_gold'])
#     return redirect("/")

def adding_gold(request):
    name='farm'
    if request.POST['sub_gold']=='farm':
        amount=random.randint(10,20)
        if 'total_gold' in request.session :
            request.session['total_gold']+=amount
     
        return redirect('/',amount,name)


    elif request.POST['sub_gold']=='cave':
        name='cave'
        amount=random.randint(5,10)
        if 'total_gold' in request.session :
            request.session['total_gold']+=amount

        return redirect('/',amount,name)

    elif request.POST['sub_gold']=='house':
        name='house'
        amount=random.randint(2,5)
        if 'total_gold' in request.session :
            request.session['total_gold']+=amount
    
        return redirect('/',amount,name)
    
    elif request.POST['sub_gold']=='casino':
        amount=random.randint(-50,50)
        if 'total_gold' in request.session :
            request.session['total_gold']+=amount
            if amount > 0:
                request.session['total_gold']+=amount
                context={
                'total_gold' : request.session['total_gold'],
                'golds_earned' : "Earned {} Golds from the casino!".format(amount),
                }
            elif amount < 0:
                request.session['total_gold']+=amount
                context={
                'total_gold' : request.session['total_gold'],
                'golds_earned' : "takes {} Golds from the casino!".format(amount),
                }
        
        return render(request,"index.html",context) 


      
        # return render('/',amount)
