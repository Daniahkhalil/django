from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('reg_log',views.register),
    path('home',views.home_page),
    path('login',views.login),
    path('logout',views.logout),
    path('add_book',views.add_book),
    path('update_fav/<int:id>',views.update_fav_book),
    path('update/<int:id>',views.update),
    path('adds_to_fav/<int:id>',views.adds_to_fav),
    path('update_this_book/<int:id>',views.update_my_book),
    path('del_this_book/<int:id>',views.delete_my_book),
    path('unfav/<int:id>',views.unfav)

    	   
]