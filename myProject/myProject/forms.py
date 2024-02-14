from django import forms
from myApp.models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class customUserForm(UserCreationForm):
    class Meta:
        model=customUser
        fields=UserCreationForm.Meta.fields + ('display_name','user_type')


class customUserAutenticationForm(AuthenticationForm):
    class Meta:
        model=customUser
        fields=['username','password']


class jobForm(forms.ModelForm):

    class Meta:
        model=JobModel
        fields=['company_name','job_position','job_place','job_type']
        lables={
            'company_name':'Enter your company_name',
            'job_position':'Enter your job_position',
            'job_place':'Enter your job_place',
            'job_type':'Enter your job_type',
        }

