from django import forms
from django.forms.models import ModelForm
from main.models1 import *
from django.core import validators
        
class UserFormSignUp(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'surname','login', 'password')
        widgets={
            'login': forms.EmailInput(),
            'password': forms.PasswordInput()
        }

class UserFormSignIn(ModelForm):
    class Meta:
        model = User
        fields = ('login', 'password')
        widgets={
            'password': forms.PasswordInput()
        }
        
class CreateTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('name',)

#update profile
class UserFormUpdateProfile(ModelForm):
    class Meta:
        model = User
        fields = ('name', 'surname','login', 'password')
        widgets = {
            'name' : forms.TextInput(),
            'surname' : forms.TextInput(),
            'login' : forms.EmailInput(),
            'password' : forms.PasswordInput()
    }

def clean_email(self):
    login = self.cleaned_data.get('login')
    password = self.cleaned_data.get('password')
    
    if login and User.objects.filter(login=login).exclude(password=password).count():
        raise forms.ValidationError('Ten login juz istnieje w bazie!')
    return login

def save(self, commit=True):
    user = super(UserFormSignUp, self).save(commit=False)
    user.login = self.cleaned_data['login']
    
    if commit:
        user.save()
    
    return user
               