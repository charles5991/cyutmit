from django.db import models
from django.forms.fields import CharField
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class DemandCategory(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class ActivityType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    
class Department(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

class Personnel(models.Model):
    name = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name


class ResearchArea(models.Model):
    name = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name
    
    
class VisitModel(models.Model):
    department = models.ManyToManyField(Department, related_name='department') #執行系所
    company = models.ForeignKey(Company) #機構
    date = models.DateField() #拜訪日期
    startTime = models.TimeField() #開始時間
    endTime = models.TimeField() #結束時間
    address = models.CharField(max_length=100) #拜訪地點
    visitNum = models.IntegerField(default=1) #拜訪次數
    teacher = models.ManyToManyField(Teacher,related_name='teacher') #拜訪教師
    personnel = models.ManyToManyField(Personnel) #拜訪對象姓名
    numCompanyPeople = models.IntegerField(default=0) #拜訪機構人數
    numSchoolPeople = models.IntegerField(default=0) #本校師生人數
    content = models.TextField() #拜訪內容
    demandCategory = models.ManyToManyField(DemandCategory) #需求類別
    researchArea = models.ManyToManyField(ResearchArea) #領域類別
    nextDate = models.DateField(null=True, blank=True) #下次拜訪日期
    followUpDepartment = models.ManyToManyField(Department) #跟進老師的所屬科系
    followUpTeacher = models.ManyToManyField(Teacher) #跟進老師
    activityType= models.ManyToManyField(ActivityType) #活動
    suggest = models.TextField() #其他建議
    
    def __str__(self):
        return self.company
    

