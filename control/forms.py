from django import forms 

class CrearEquipo(forms.Form):
    campeon = forms.CharField(required=True, max_length=100)
    subcampeon = forms.CharField(required=True, max_length=100)
    año = forms.IntegerField(required=True, max_value=20000)
    sede = forms.CharField(required=True, max_length=250)

class CrearSeleccion(forms.Form):
    seleccion = forms.CharField(required=True, max_length=100)
    ganados = forms.IntegerField(required=True, max_value=20000)
    empatados = forms.IntegerField(required=True, max_value=20000)
    perdidos = forms.IntegerField(required=True, max_value=20000)
    puntos = forms.IntegerField(required=True, max_value=20000)
