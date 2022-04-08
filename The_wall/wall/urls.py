from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('reg_log', views.regiser),  
    path('login', views.login),
    path('logout',views.logout),
    path('message',views.message),
    path('comment',views.comment_),
    path('delete',views.delete)
]