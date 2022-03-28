from django.shortcuts import redirect, render
from time import gmtime, strftime

def index(request):
   
    #declare session
    if 'count' in request.session:

        request.session['count']+=2
        return render(request,'index.html')


    else :
        request.session['count']=-2
        return redirect('/')
    
def mypost(request):
    # if request.POST['button']=="Add Two Visits":
    #     request.session['count']+=2
    # else:
    if request.POST['button']=="reset":
        request.session['count']=-2
    
        # if 'addtwovisits' in request.POST:
        #     request.session['count']+=2
        #     return render(request,'index.html')
              
        # elif 'reset' in request.POST:
        #         request.session['count']=-2
                # return redirect('/destroy_session')
    return redirect('/')










    
# def index(request):
    
#     if 'count' in request.session:
#         if request.method=='GET':
#             request.session['count']+=1
#             return render(request,'index.html')
            
            
#         else:
#             if 'addtwovisits' in request.POST:
#                 request.session['count']+=1

#             elif 'reset' in request.POST:
#                 request.session['count']=-1
#             return redirect('/post')
            
            

        
#     else:
#         request.session['count']=-1
#         return render(request,'index.html')
# def mypost(request):
#     return redirect('/')
