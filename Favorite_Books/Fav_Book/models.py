from django.db import models
import re
class UserManager(models.Manager):
        def basic_validator(self, postData):
            errors = {}
            if(postData['first_name'].isalpha()) == False:
                errors["first_name"] = "Enter a valid first name."
        # add keys and values to errors dictionary for each invalid field
            if len(postData['first_name']) < 2:
                errors["first_name"] = "first name should be at least 2 characters"

            if(postData['last_name'].isalpha()) == False:
                errors["last_name"] = "Enter a valid last name."
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
class BookManager(models.Manager):
        def book_validator(self, postData):
            errors = {}
            if(postData['title'].isalpha()) == False:
                errors["title"] = "Enter a valid title name."
            if len(postData['title']) < 2:
                errors["title"] = "first title should be at least 2 characters"

            if len(postData['desc']) < 2:
                errors["desc"] = "first description should be at least 2 characters"
            return errors


class User(models.Model):
    first_name=models.CharField(max_length=45 , null=False)
    last_name=models.CharField(max_length=45, null=False)
    email=models.CharField(max_length=255, null=False)
    password=models.CharField(max_length=45, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =UserManager()

class Book(models.Model):
    title=models.CharField(max_length=45, null=False)
    desc=models.CharField(max_length=255, null=False)
    uploaded_by=models.ForeignKey(User,related_name="books_uploaded",on_delete = models.CASCADE)
    users_who_liked=models.ManyToManyField(User,related_name="liked_books",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =BookManager()
