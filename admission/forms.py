from django.forms import ModelForm
from django.contrib.auth.models import User


class PreApplicationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']