from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('number_game', views.number_game),
    path('result', views.result_game),
]