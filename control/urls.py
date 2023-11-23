from django.urls import path
from control.views import selecciones, copa

urlpatterns = [
    path("selecciones/", selecciones),
    path("copa/", copa),
]