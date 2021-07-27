from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria =models.CharField(max_length=50)

    def __str__(self):
        return self.nombreCategoria

class Login(models.Model):
    correo = models.CharField(max_length=40, primary_key=True)
    contraseña = models.CharField(max_length=20)
    
    def __str__(self):
        return self.correo