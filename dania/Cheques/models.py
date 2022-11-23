# Create your models here.

from django.db import models
import re
import datetime


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


class ChequeManager(models.Manager):
        def cheque_validator(self, postData):
            errors = {}
            if(postData['name'].isalpha()) == False:
                errors["name"] = "Enter a valid name."
            if len(postData['name']) < 4:
                errors["name"] = "Name should be at least 4 characters"

            if(postData['bankname'].isalpha()) == False:
                errors["bankname"] = "Enter a valid bank name."
            if len(postData['bankname']) < 3:
                errors["bankname"] = "bank name should be at least 3 characters"

            if(postData['branchname'].isalpha()) == False:
                errors["branchname"] = "Enter a valid branch name."
            if len(postData['branchname']) < 3:
                errors["branchname"] = "Branch name should be at least 3 characters"
            
            if(int(postData['chequenumber'] ) < 0) :
                errors["chequenumber"] = "Enter a valid cheque number."
            
            if(int(postData['price'] )< 0) :
                errors["price"] = "Enter a valid price."

            if(postData['status'].isalpha()) == False:
                errors["status"] = "Enter a valid status."
            if len(postData['status']) < 6:
                errors["status"] = "Name should be at least 6 characters"

            if(postData['chequedate']  > postData['returneddate'] ):
                errors["status"] = "Cheque date must be less than returend date"

            return errors

class BillManager(models.Manager):
        def bill_validator(self, postData):
            errors = {}
            if(postData['draftname'].isalpha()) == False:
                errors["draftname"] = "Enter a valid name."
            if len(postData['draftname']) < 4:
                errors["draftname"] = "Name should be at least 4 characters"
            
            if(int(postData['draftnumber']) < 0) :
                errors["draftnumber"] = "Enter a valid bill number."
            
            if(int(postData['draftprice']) < 0) :
                errors["draftprice"] = "Enter a valid price."

            if(postData['draftstatus'].isalpha()) == False:
                errors["draftstatus"] = "Enter a valid status."
            if len(postData['draftstatus']) < 3:
                errors["draftstatus"] = "Name should be at least 3 characters"
        

            return errors

class Cheque(models.Model):
    chequename = models.CharField(max_length=45)
    chequedate = models.DateTimeField(default=datetime.date.today(),null=False)
    returneddate = models.DateTimeField(null=False)
    chequenumber=models.IntegerField(null=False)
    chequeprice=models.FloatField(null=False)
    chequestatus=models.TextField(max_length=45,null=False)
    bankname=models.TextField(max_length=45 , null=False)
    branchname=models.TextField(max_length=45,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =ChequeManager()

class Bill(models.Model):
    billame = models.CharField(max_length=45)
    billdate = models.DateTimeField(default=datetime.date.today(),null=False)
    billnumber=models.IntegerField(null=False)
    billprice=models.FloatField(null=False)
    billstatus=models.TextField(max_length=45,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =BillManager()
    
class User(models.Model):
    first_name=models.CharField(max_length=45 , null=False)
    last_name=models.CharField(max_length=45 , null=False)
    email=models.CharField(max_length=255, null = False)
    password=models.CharField(max_length=45 , null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects =UserManager()
