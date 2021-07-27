from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Login(models.Model):
    correo = models.ForeignKey(Registro, on_delete=models.PROTECT)
    contraseña = models.CharField(max_length=20)

    def __str__ (self):
        return self.correo

opciones_consultas =[
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencia"],
    [3, "felicitaciones"]
]
class Contacto(models.Model):
    nombre =models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre