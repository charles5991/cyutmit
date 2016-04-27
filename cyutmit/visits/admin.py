from django.contrib import admin
from visits.models import DemandCategory, Department, Teacher, Company, Personnel, ActivityType, ResearchArea
# Register your models here.

admin.site.register(DemandCategory)
admin.site.register(Teacher)
admin.site.register(Company)
admin.site.register(Personnel)
admin.site.register(ActivityType)
admin.site.register(ResearchArea)
admin.site.register(Department)