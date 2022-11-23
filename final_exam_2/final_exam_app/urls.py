from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('reg_log',views.register),
    path('home',views.home_page),
    path('login',views.login),
    path('logout',views.logout),
    path('add_car',views.show_add),
    path('add_car_to_dashboard', views.add_car),
    path('edit_my_car/<int:id>',views.edit_car),
    path('back_to_dashboard', views.back_to_dashboard),
    path('update_my_car/<int:id>',views.update_my_car),
    path('delete_my_car/<int:id>',views.delete_my_car),
    path('display_car/<int:id>',views.dispaly_car),
    path('delete_from_db/<int:id>',views.delete_my_car)

    	   
]