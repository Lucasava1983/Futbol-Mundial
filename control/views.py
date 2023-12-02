from django.shortcuts import render, redirect
from django.urls import reverse
from control.models import Clasificatorias, Copa_Libertadores, Noticias
from control.forms import CrearEquipo, CrearSeleccion
from django.db.models import Q
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView

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
        formulario = CrearEquipo(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            campeon = data["campeon"]
            subcampeon = data["subcampeon"]
            año = data["año"]
            estadio = data["estadio"]
            cupos = Copa_Libertadores(campeon=campeon, subcampeon=subcampeon, año=año, estadio=estadio)
            cupos.save()
            url_exitosa = reverse('copa')
            return redirect(url_exitosa)
    else:
            formulario=CrearEquipo()
            http_response = render(
            request=request,
            template_name='control/formulario_equipos.html',
            context={'formulario':formulario }
    )
    return http_response

def crear_seleccion(request):
    if request.method == "POST":
       formulario = CrearSeleccion(request.POST)
       if formulario.is_valid():
            data = formulario.cleaned_data
            seleccion = data["seleccion"]
            ganados = data["ganados"]
            empatados = data["empatados"]
            perdidos = data["perdidos"]
            puntos = data["puntos"]
            equipos = Clasificatorias(seleccion=seleccion, ganados=ganados, empatados=empatados, perdidos=perdidos, puntos=puntos)
            equipos.save()
            url_exitosa = reverse('selecciones')
            return redirect(url_exitosa)
    else:
        formulario=CrearSeleccion()
        http_response = render(
        request=request,
        template_name='control/formulario_selecciones.html',
        context={'formulario':formulario }
    )
    return http_response

def buscar_equipos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        
        cupos = Copa_Libertadores.objects.filter(
            Q(campeon__contains=busqueda) | Q(subcampeon__contains=busqueda) | Q(año__contains=busqueda) | Q(estadio__contains=busqueda)
        )
        
        contexto = {
            "cupos": cupos,
        }
        
        http_response = render(
            request=request,
            template_name='control/lista_equipos.html',
            context=contexto,
        )
        
        return http_response
    
def buscar_seleccion(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        
        equipos = Clasificatorias.objects.filter(
            Q(seleccion__contains=busqueda) | Q(ganados__contains=busqueda) | Q(empatados__contains=busqueda) | Q(perdidos__contains=busqueda) | Q(puntos__contains=busqueda)
        )
        
        contexto = {
            "equipos": equipos,
        }
        
        http_response = render(
            request=request,
            template_name='control/lista_selecciones.html',
            context=contexto,
        )
        
        return http_response
    
def eliminar_equipo(request, id):
    cupos = Copa_Libertadores.objects.get(id=id)
    if request.method == "POST":
        
        cupos.delete()
        
        url_exitosa = reverse('copa')
        return redirect(url_exitosa)
    
def eliminar_seleccion(request, id):
    equipos = Clasificatorias.objects.get(id=id)
    if request.method == "POST":
        
        equipos.delete()
        
        url_exitosa = reverse('selecciones')
        return redirect(url_exitosa)
    
def editar_equipo(request, id):
    cupos = Copa_Libertadores.objects.get(id=id)
    if request.method == "POST":
        formulario = CrearEquipo(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            cupos.campeon = data['campeon']
            cupos.subcampeon = data['subcampeon']
            cupos.año = data['año']
            cupos.estadio = data['estadio']
            cupos.save()
            
            url_exitosa = reverse('copa')
            return redirect(url_exitosa)
    else:
        inicial = {
            'campeon': cupos.campeon,
            'subcampeon': cupos.subcampeon,
            'año': cupos.año,
            'estadio': cupos.estadio,
        }          
        
        formulario = CrearEquipo(initial=inicial)
    return render(
        request=request,
        template_name='control/formulario_equipos.html',
        context={'formulario': formulario},
    )
    
def editar_seleccion(request, id):
    equipos = Clasificatorias.objects.get(id=id)
    if request.method == "POST":
        formulario = CrearSeleccion(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            equipos.seleccion = data['seleccion']
            equipos.ganados = data['ganados']
            equipos.empatados = data['empatados']
            equipos.perdidos = data['perdidos']
            equipos.puntos = data['puntos']
            equipos.save()
            
            url_exitosa = reverse('selecciones')
            return redirect(url_exitosa)
    else:
        inicial = {
            'seleccion': equipos.seleccion,
            'ganados': equipos.ganados,
            'empatados': equipos.empatados,
            'perdidos': equipos.perdidos,
            'puntos': equipos.puntos,
        }          
        
        formulario = CrearSeleccion(initial=inicial)
    return render(
        request=request,
        template_name='control/formulario_selecciones.html',
        context={'formulario': formulario},
    )
    
    