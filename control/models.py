from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Noticias(models.Model):
    titulo=models.CharField(max_length=150)
    subtitulo=models.CharField(max_length=200)
    articulo=models.CharField(max_length=1500)
    autor=models.CharField(max_length=250)
    fecha=models.DateTimeField(auto_now=True)
    imagen=models.ImageField(upload_to='fotos')
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.titulo}, {self.subtitulo}, {self.imagen}, {self.fecha}'

class Clasificatorias(models.Model):
    seleccion=models.CharField(max_length=100)
    ganados=models.IntegerField()
    empatados=models.IntegerField()
    perdidos=models.IntegerField()
    puntos=models.IntegerField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.seleccion}, {self.puntos}'

class Copa_Libertadores(models.Model):
    campeon=models.CharField(max_length=150)
    subcampeon=models.CharField(max_length=150)
    año=models.IntegerField()
    estadio=models.CharField(max_length=250)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.campeon}, {self.año}'
    
