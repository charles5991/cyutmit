import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cyutmit.settings')
import django
django.setup()

from visits.models import VisitModel, DemandCategory, Department, Teacher, Company, Personnel, ActivityType, ResearchArea
import random

def populate():
    # DemandCategory
    demandCategory = addDemandCategory('人才招募')
    demandCategory = addDemandCategory('學期實習/建教合作')
    demandCategory = addDemandCategory('產學合作')
    demandCategory = addDemandCategory('人才培訓')
    demandCategory = addDemandCategory('其他')
    
    # ActivityType
    activityType = addActivityType('演講')
    activityType = addActivityType('諮詢')
    activityType = addActivityType('座談')
    activityType = addActivityType('業師')
    activityType = addActivityType('轉借他系')
    
    # Department 
    department = addDepartment('資管系')
    department = addDepartment('資工系')
    department = addDepartment('資通系')
    
    # Teacher 
    teacher = addTeacher('唐元亮')
    teacher = addTeacher('薛夙珍')
    teacher = addTeacher('李富民')
    
    # Company
    company = addCompany('統一企業')
    company = addCompany('鼎新')
    company = addCompany('國興')
    
    # Personnel
    personnel = addPersonnel('王小明')
    personnel = addPersonnel('王中明')
    personnel = addPersonnel('王大明')
    
    # ResearchArea
    researchArea = addResearchArea('雲端')
    researchArea = addResearchArea('大數據')
    researchArea = addResearchArea('物聯網')
    researchArea = addResearchArea('智慧製造')
    researchArea = addResearchArea('系統開發')
    
    
    # Print DemandCategory
    for  demandCategory in DemandCategory.objects.all():
        print('需求類別:'+demandCategory.name)
        
    # Print ActivityType
    for  activityType in ActivityType.objects.all():
        print('活動:'+activityType.name)      
    
def addDemandCategory(name):
    demandCategory = DemandCategory.objects.get_or_create(name=name)[0]
    return demandCategory  


def addActivityType(name):
    activityType = ActivityType.objects.get_or_create(name=name)[0]
    return activityType


def addDepartment(name):
    department = Department.objects.get_or_create(name=name)[0]
    return department


def addTeacher(name):
    teacher = Teacher.objects.get_or_create(name=name)[0]
    return teacher


def addCompany(name):
    company = Company.objects.get_or_create(name=name)[0]
    return company


def addPersonnel(name):
    personnel = Personnel.objects.get_or_create(name=name)[0]
    return Personnel


def addResearchArea(name):
    researchArea = ResearchArea.objects.get_or_create(name=name)[0]
    return researchArea




if __name__ == '__main__':
    print('開始填入資料...')
    populate()
    print('完成。')