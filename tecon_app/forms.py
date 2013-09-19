# coding: utf-8

from django.forms import ModelForm, TextInput
from tecon_app.models import Trial


class TrialForm(ModelForm):
    class Meta:
        model = Trial
        fields = ['title', 'description', 'category']
        widgets = {
            'title': TextInput(attrs={'required': ''}),
        }
