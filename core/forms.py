from django import forms
from django import forms
from django.forms import ModelForm, fields, widgets
from .models import Registro, Login, Contacto

class RegistroForm(ModelForm):

    class Meta:
        model = Registro
        fields= ['nombre', 'correo', 'contraseña']
        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields= ['correo', 'contraseña']
        widgets={
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        widgets ={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            
            'mensaje': forms.Textarea(attrs={'class': 'form-control'}),
            'aviso': forms.Select(attrs={'class': 'form-control'}),
        }