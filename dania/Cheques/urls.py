from django.urls import path
from . import views


from django.contrib import admin
from django.urls import path

from django.urls import include, re_path


urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('reg_log',views.register),
    path('login',views.login),
    path('logout',views.logout),
    path('home/cheque', views.cheque),
    path('home/draft', views.draft),
    path('home/cheque/addcheque',views.addcheque),
    path('home/draft/adddraft',views.adddraft),
    path('home/display_cheque/edit_my_cheque/<int:id>',views.edit_cehque),
    path('home/display_cheque/edit_my_cheque/home/display_cheque/update_my_cheque/<int:id>',views.update_my_cheque),
    path('home/display_cheque',views.dispaly_cheque),
    path('home/display_draft/delete_from_db/<int:id>',views.delete_my_draft),
    path('home/display_draft/edit_my_draft/<int:id>',views.edit_draft),
    path('home/display_draft/edit_my_draft/home/display_draft/update_my_draft/<int:id>',views.update_my_draft),
    path('home/display_draft',views.dispaly_draft),
    path('home/display_draft/delete_from_db/<int:id>',views.delete_my_draft),
    path('home/display_cheque/delete_from_db/<int:id>',views.delete_my_cheque),
   
    path('admin/', admin.site.urls),
    path('home/reg_log',views.reg,name='reg_log')
   
 
    

]