from turtle import title
from django.db import models

# Create your models here.
class book(models.Model) :  
    title=models.CharField(max_length=45)
    desc=models.TextField(default="book description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class authors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    note=models.TextField(default="notes")
    books=models.ManyToManyField(book,related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def list_of_Books():
    return book.objects.all()


def list_of_authors():
    return authors.objects.all()