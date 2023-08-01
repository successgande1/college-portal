from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from academics.models import CourseOfStudy
from django import forms

class PreApplicationForm(UserCreationForm):
    course_name = forms.ModelChoiceField(queryset=CourseOfStudy.objects.all())
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] 

        