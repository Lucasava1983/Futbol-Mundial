from django.shortcuts import render, redirect
from django.urls import reverse
from control.models import Clasificatorias, Copa_Libertadores, Noticias

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

def Inicio(request):
    contexto = {
        "noticia": Noticias.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='inicio.html',
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
        url_exitosa = reverse('copa')
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
       equipos = Clasificatorias(seleccion=data['seleccion'], ganados=data['ganados'], empatados=data['empatados'], perdidos=data['perdidos'], puntos=data['puntos'])
       equipos.save()
       url_exitosa = reverse('selecciones')
       return redirect(url_exitosa)
    else:
            http_response = render(
            request=request,
            template_name='control/formulario_selecciones.html',
    )
    return http_response

