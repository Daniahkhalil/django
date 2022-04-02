from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/process_mony',views.adding_gold),
  
]