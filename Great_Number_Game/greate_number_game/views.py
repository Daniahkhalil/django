from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    request.session['random_number'] = random.randint(1, 100)
    if 'guess' in request.session:
        del request.session['guess']
    if 'counter' in request.session:
        del request.session['counter']
    return render(request,"index.html")
    

def number_game(request): 
    request.session['guess'] = int (request.POST["randomint"]) 
    if not 'counter' in request.session :
        request.session['counter'] = 0
    else:
        request.session['counter'] += 1
    print(request.session['random_number'])
    print(request.session['guess']) 
    return redirect("/result")

def result_game(request):
    return render(request, "index.html")

  


    
