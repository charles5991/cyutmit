from django.db import models

# Create your models here.
class DemandCategory(models.Model):
    name = models.CharField(max_length=50) #需求類別名稱
    
    def __str__(self):
        return self.name
    

class ActivityType(models.Model):
    name = models.CharField(max_length=50) #活動名稱
    
    def __str__(self):
        return self.name

    
class Department(models.Model):
    name = models.CharField(max_length=50) #科系
    
    def __str__(self):
        return self.name       


class ResearchArea(models.Model):
    name = models.CharField(max_length=50) #研究領域名稱
    
    def __str__(self):
        return self.name