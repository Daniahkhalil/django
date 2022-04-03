from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	
    path('Add_book',views.adding_book) , 
    path('books/<int:id>/',views.view_book),
    path('books/add_author/<int:id>',views.adding_author),
    path('author',views.view_authors),
    path('Add_author',views.adding_author2)
]