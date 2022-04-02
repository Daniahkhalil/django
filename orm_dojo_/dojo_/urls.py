from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	 
    path('Add_dojo', views.add_dojo),  
    path('Add_ninja', views.add_ninja),  
    
]