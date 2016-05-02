from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.forms.fields import CharField

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50) #廠商
    
    def __str__(self):
        return self.name
    
    
class Personnel(models.Model):
    name = models.CharField(max_length=50) #聯絡人姓名
    
    def __str__(self):
        return self.name    