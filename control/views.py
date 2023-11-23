from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def selecciones(request):
    contexto = {
        "equipos": "Nacional",
    }
    http_response = render(
        request=request,
        template_name='lista_selecciones.html',
        context=contexto,
    )
    return http_response

def copa(request):
    contexto = {
        "cupos": "Nacional",
    }
    http_response = render(
        request=request,
        template_name='lista_equipos.html',
        context=contexto,
    )
    return http_response
# Create your views here.
