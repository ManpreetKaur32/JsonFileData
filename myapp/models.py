from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import json

# Create your models here.
class mydata(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    Phone=models.IntegerField()
    Ratings=models.DecimalField(max_digits=5, decimal_places=2)
    Reviews=models.CharField(max_length=100)
    Description=models.TextField(max_length=200)

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self,name,max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT,name))
        return name
        
class JsonFile(models.Model):
    upload_file = models.FileField(storage=OverwriteStorage(),upload_to='file_media/')
    
class Customer(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=200)
    Phone=models.IntegerField()
    Ratings=models.DecimalField(max_digits=5, decimal_places=2)
    Reviews=models.CharField(max_length=100)
    Description=models.TextField(max_length=200)

