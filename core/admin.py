from core.models import Categoria
from django.contrib import admin
from .models import Categoria, Login

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Login)