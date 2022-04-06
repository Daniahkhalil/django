
from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
        def basic_validator(self, postData):
            errors = {}
        # add keys and values to errors dictionary for each invalid field
            if len(postData['first_name']) < 2:
                errors["first_name"] = "first name should be at least 2 characters"
            if len(postData['last_name']) < 2:
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



class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =UserManager()

