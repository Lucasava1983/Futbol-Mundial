from django.db import models

# Create your models here.
class Noticia(models.Model):
    titulo=models.CharField(max_length=150)
    subtitulo=models.CharField(max_length=200)
    articulo=models.CharField(max_length=1500)
    autor=models.CharField(max_length=250)
    fecha=models.DateTimeField(auto_now=True)
    imagen=models.ImageField(upload_to='fotos')

class Clasificatorias(models.Model):
    seleccion=models.CharField(max_length=100)
    partidos_ganados=models.IntegerField()
    partidos_empatados=models.IntegerField()
    partidos_perdidos=models.IntegerField()
    puntos=models.IntegerField()

class Copa_Libertadores(models.Model):
    campeon=models.CharField(max_length=150)
    subcampeon=models.CharField(max_length=150)
    año=models.DateField(null=True)
    sede=models.CharField(max_length=250)
