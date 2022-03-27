from django.shortcuts import render,HttpResponse ,redirect
def test(request):
    return redirect("blogs")

def root(request):
    return HttpResponse("this is the equivalent of @app.route('/blogs')!")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request,number):
    print(number)
    return HttpResponse("placeholder to display blog number: "+ number )

def edit(request,number):
    print(number)
    return HttpResponse("placeholder to display blog number: "+ number )

def destroy(request,number):
    return redirect("blogs")