from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.forms.fields import CharField

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50) #姓名
    
    def __str__(self):
        return self.name