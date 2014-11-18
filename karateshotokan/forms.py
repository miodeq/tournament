from django import forms
from django.forms.models import ModelForm
from main.models1 import *
from django.core import validators
from django.utils import dateformat
        
class CreateTournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields= ('name', 'start', 'end' )
        widgets={
            'start': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker'}),
            'end': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'datepicker'})
        }

