from django import forms
from django.db.models.base import Model  
from django.forms import ModelForm
from .models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ['correo', 'contraseña']