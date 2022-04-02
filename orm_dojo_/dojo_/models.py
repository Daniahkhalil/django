from pyexpat import model
from sre_parse import State
from unicodedata import name
from venv import create
from django.db import models

# Create your models here.
class Dojo(models.Model):
    name=models.CharField(max_length=45)
    city=models.CharField(max_length=255)
    State=models.CharField(max_length=2)
    desc=models.TextField(default='old dojo')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
class Ninja(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    dojo=models.ForeignKey(Dojo,related_name="dojos",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


def list_of_all_dojos():
    return Dojo.objects.all()

# def create_dojo():

