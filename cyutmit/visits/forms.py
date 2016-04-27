from django import forms
from django.forms.widgets import TextInput, Textarea

from visits.models import VisitModel, DemandCategory, Department, Teacher, Company, Personnel, ActivityType, ResearchArea


class VisitForm(forms.ModelForm):
    department = forms.ModelMultipleChoiceField(label='執行系所', queryset=Department.objects.all(), widget=forms.CheckboxSelectMultiple)
    date = forms.DateField(label='拜訪日期', widget=TextInput(attrs={'type':'date'}))
    startTime = forms.TimeField(label='開始時間', widget=TextInput(attrs={'type':'time'}))
    endTime = forms.TimeField(label='結束時間', widget=TextInput(attrs={'type':'time'}))
    company = forms.ModelChoiceField(label='機構', queryset=Company.objects.all())
    address = forms.CharField(label='地址', widget=Textarea(attrs={'rows':5, 'cols':20}))
    visitNum = forms.IntegerField(label='拜訪次數')
    teacher = forms.ModelMultipleChoiceField(label='拜訪老師', queryset=Teacher.objects.all(), widget=forms.CheckboxSelectMultiple)
    personnel = forms.ModelMultipleChoiceField(label='拜訪對象姓名', queryset=Personnel.objects.all(), widget=forms.CheckboxSelectMultiple)
    numCompanyPeople = forms.IntegerField(label='拜訪機構人數')
    numSchoolPeople = forms.IntegerField(label='本校師生人數')
    content = forms.CharField(label='拜訪內容', widget=Textarea(attrs={'rows':5, 'cols':20}))
    demandCategory = forms.ModelMultipleChoiceField(label='需求歸屬類別', queryset=DemandCategory.objects.all(), widget=forms.CheckboxSelectMultiple)
    researchArea = forms.ModelMultipleChoiceField(label='領域類別', queryset=ResearchArea.objects.all(), widget=forms.CheckboxSelectMultiple)
    nextDate = forms.DateField(label='下次拜訪日期', widget=TextInput(attrs={'type':'date'}), required=False)
    followUpDepartment = forms.ModelMultipleChoiceField(label='委託科系', queryset=Department.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    followUpTeacher = forms.ModelMultipleChoiceField(label='委託教師', queryset=Teacher.objects.all(), widget=forms.CheckboxSelectMultiple,required=False)
    activityType = forms.ModelMultipleChoiceField(label='活動', queryset=ActivityType.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    suggest = forms.CharField(label='其他建議', widget=Textarea(attrs={'rows':5, 'cols':20}), required=False)
    
    class Meta:
        model = VisitModel
        fields = '__all__'