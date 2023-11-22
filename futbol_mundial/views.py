from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def saludar_con_html(request):
    contexto = {
        "equipo": "Nacional",
    }
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response
