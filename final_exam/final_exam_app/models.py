
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
        def basic_validator(self, postData):
            errors = {}
        # add keys and values to errors dictionary for each invalid field
                      
            if(postData['first_name'].isalpha()) == False:
                errors["first_name"] = "Enter a valid first name."
            if len(postData['first_name']) < 3:
                errors["first_name"] = "first name should be at least 3 characters"
            
            if(postData['last_name'].isalpha()) == False:
                errors["last_name"] = "Enter a valid last name."
            if len(postData['last_name']) < 3:
                errors["last_name"] = "last name should be at least 2 characters"

            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
                errors['email'] = "Invalid email address!"
            if len(postData['passward']) < 8:
                errors["passward"] = "passward should be at least 8 characters"
            if len(postData['confirm_password']) < 8:
                errors["confirm_password"] = "confirm passward should be at least 8 characters"
            if postData['passward'] != postData['confirm_password']:
                errors["confirm_password"] = "passward and confirm passward not matched"
  

            return errors
        
        def log_validator(self, postData):
            errors = {}
                   # add keys and values to errors dictionary for each invalid field
            EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
            if not EMAIL_REGEX.match(postData['email_log']):    # test whether a field matches the pattern            
                errors['email_log'] = "Invalid email address!"
            if len(postData['Passward_log']) < 8:
                errors["Passward_log"] = "passward should be at least 8 characters"

            return errors

class CarManager(models.Manager):
        def car_validator(self, postData):
            errors = {}
            if(postData['model'].isalpha()) == False:
                errors["model"] = "Enter a valid model."
            if len(postData['model']) < 3:
                errors["model"] = "first name should be at least 3 characters"

            if(postData['make'].isalpha()) == False:
                errors["make"] = "Enter a valid last make."
            if len(postData['make']) < 3:
                errors["make"] = "Make should be at least 3 characters"

            if(postData['desc'].isalpha()) == False:
                errors["desc"] = "Enter a valid last desc."
            if len(postData['desc']) < 8:
                errors["desc"] = "Description should be at least 8 characters"

            
        
            return errors



class User(models.Model):
    first_name=models.CharField(max_length=45 , null=False)
    last_name=models.CharField(max_length=45 , null=False)
    email=models.CharField(max_length=255, null = False)
    password=models.CharField(max_length=45 , null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =UserManager()

class Car(models.Model):
    price=models.FloatField(null=False)
    model=models.CharField(max_length=45, null=False)
    make=models.CharField(max_length=45, null=False)
    year=models.DateField(null=False)
    desc=models.CharField(max_length=100, null=False)
    seller=models.ForeignKey(User, related_name="cars" , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =CarManager()