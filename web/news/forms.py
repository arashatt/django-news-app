#forms.py
from django import forms
from django.forms import ModelForm
from .models import News
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['NewsTitle', 'NewsClass', 'NewsBody', 'slug']
    
