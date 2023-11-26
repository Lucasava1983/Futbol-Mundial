from django.urls import path
from control.views import selecciones, copa, crear_equipo, crear_seleccion
urlpatterns = [
    path("selecciones/", selecciones, name="selecciones"),
    path("copa/", copa, name="copa"),
    path("crear-equipo/", crear_equipo, name="crear_equipo"),
    path("crear-seleccion/", crear_seleccion, name="crear_seleccion"),
]