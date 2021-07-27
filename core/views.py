from core import forms
from django.shortcuts import render
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def shop(request):
    return render(request, 'core/shop.html')

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            data['form'] = formulario
            data['mensaje'] = "Se envio el Formulario!"
        else:
            data['form'] = ContactoForm()
    return render(request, 'core/contact.html', data)

def login(request):
    datos ={
        'form': LoginForm()
    }
    return render(request, 'core/login.html', datos)

def register(request):
    datos = {
        'form': RegistroForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['form'] = formulario
            datos['mensaje'] = "Datos grabados!"
    else:
        datos['form'] = RegistroForm()
    return render(request, 'core/register.html', datos)
