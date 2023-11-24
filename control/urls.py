from django.urls import path
from control.views import selecciones, copa

urlpatterns = [
    path("selecciones/", selecciones, name="selecciones"),
    path("copa/", copa, name="copa"),
]