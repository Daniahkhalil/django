from django.urls import path     
from . import views

urlpatterns = [
    path('show', views.index),
    path('show/<int:id>', views.book_details),
    path('show/<int:id>/edit', views.show_edit),
    path('updated/<int:id>', views.updated),
    path('show/<int:id>/delete', views.delete_show),
    path('show/create', views.create_show),
    path('create', views.create),
    path('create/go_back',views.go_back),
    path('show/go_back',views.go_back)



]