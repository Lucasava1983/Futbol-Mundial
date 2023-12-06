from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from control.models import Noticias
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


#def Inicio(request):
#    contexto = {
#        "noticia": Noticias.objects.all(),
#    }
#    http_response = render(
#        request=request,
#        template_name='inicio.html',
#        context=contexto,
#    )
#    return http_response


class InicioListView(ListView):
    model = Noticias
    template_name ='inicio.html'
    
class InicioCreateView(LoginRequiredMixin, CreateView):
    model = Noticias
    success_url = reverse_lazy
    
class InicioDetailView(LoginRequiredMixin, DetailView):
    model = Noticias
    success_url = reverse_lazy
    