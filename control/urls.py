from django.urls import path
from control.views import selecciones, copa, crear_equipo, crear_seleccion, buscar_equipos, buscar_seleccion
urlpatterns = [
    path("selecciones/", selecciones, name="selecciones"),
    path("copa/", copa, name="copa"),
    path("crear-equipo/", crear_equipo, name="crear_equipo"),
    path("crear-seleccion/", crear_seleccion, name="crear_seleccion"),
    path("buscar-equipos/", buscar_equipos, name="buscar_equipos"),
    path("buscar-seleccion/", buscar_seleccion, name="buscar_seleccion"),
]