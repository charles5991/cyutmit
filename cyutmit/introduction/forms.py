from django import forms
from main.views import customErrors
from introduction.models import Introduction


class IntroductionsForm(forms.ModelForm):
    title = forms.CharField(max_length=128, label='標題', error_messages=customErrors)
    content = forms.CharField(widget=forms.Textarea, label='內容', error_messages=customErrors)
    
    class Meta:
        model = Introduction
        fields = ('title', 'content')

    