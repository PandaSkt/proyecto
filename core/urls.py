from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tienda', views.shop, name='shop'),
    path('nosotros', views.about, name='about'),
    path('contacto', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]