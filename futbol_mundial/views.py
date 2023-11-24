from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from control.models import Noticias

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
