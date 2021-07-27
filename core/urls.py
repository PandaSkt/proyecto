from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tienda', views.shop, name='shop'),
    path('nosotros', views.about, name='about'),
    path('contacto', views.contact, name='contact'),
    path('ingresar', views.ingresar, name='ingresar'),
    path('register', views.register, name='register'),
]