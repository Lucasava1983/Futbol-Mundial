from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime
from control.models import Clasificatorias, Copa_Libertadores

def selecciones(request):
    contexto = {
        "equipos": Clasificatorias.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control/lista_selecciones.html',
        context=contexto,
    )
    return http_response

def copa(request):
    contexto = {
        "cupos": Copa_Libertadores.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control/lista_equipos.html',
        context=contexto,
    )
    return http_response
# Create your views here.
def crear_equipo(request):
    if request.method == "POST":
        data = request.POST
        cupos = Copa_Libertadores(campeon=data['campeon'], subcampeon=data['subcampeon'], año=data['año'], sede=data['sede'])
        cupos.save()
        url_exitosa = reverse('lista_equipos')
        return redirect(url_exitosa)
    else:
        http_response = render(
        request=request,
        template_name='control/formulario_equipos.html',
    )
    return http_response

def crear_seleccion(request):
    if request.method == "POST":
       data = request.POST
       cupos = Clasificatorias(seleccion=data['seleccion'], partidos_ganados=data['partidos_ganados'], partidos_empatados=data['partidos_empatados'], partidos_perdidos=data['partidos_perdidos'], puntos=data['puntos'])
       cupos.save()
       url_exitosa = reverse('lista_selecciones')
       return redirect(url_exitosa)
    else:
        http_response = render(
        request=request,
        template_name='control/formulario_selecciones.html',
    )
    return http_response

