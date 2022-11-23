from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('reg_log',views.register,name='reg_log'),
    path('home',views.home_page),
    path('login',views.login),
    path('logout',views.logout)

    	   
]