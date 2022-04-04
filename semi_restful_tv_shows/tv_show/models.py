from platform import release
from pyexpat import model
from django.db import models


# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 2 characters"
        return errors

class Show(models.Model):
    title=models.CharField(max_length=100)
    network=models.CharField(max_length=10)
    release_date=models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = ShowManager()    # add this line!

# return all shows objects
def list_of_shows():
    return Show.objects.all()

    

