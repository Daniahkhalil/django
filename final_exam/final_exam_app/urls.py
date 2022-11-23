from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('reg_log',views.register),
    path('home',views.home_page),
    path('login',views.login),
    path('logout',views.logout),
    path('add_car',views.show_add),
    path('add_car_to_dashboard', views.add_car)


    	   
]